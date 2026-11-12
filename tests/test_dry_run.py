#!/usr/bin/env python3
"""不需要 Key 的演练测试：检查汽车选题监控的目录结构、技能文件和运行日志。

  python3 tests/test_dry_run.py
"""
import json
import os
import py_compile
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOT = ROOT / 'bots' / 'auto-topic-monitor'


class BotStructure(unittest.TestCase):
    def test_required_files(self):
        required = [
            'README.md',
            'job.md',
            'routines.md',
            'check.md',
            'skills/auto-topic-monitor/SKILL.md',
            'skills/douyin-comments/SKILL.md',
            'templates/每日播报模板.md',
            'templates/内容拆解模板.md',
            'templates/选题台账模板.csv',
        ]
        for name in required:
            self.assertTrue((BOT / name).is_file(), f'missing {name}')

    def test_skill_frontmatter(self):
        text = (BOT / 'skills' / 'auto-topic-monitor' / 'SKILL.md').read_text(encoding='utf-8')
        self.assertIn('name: auto-topic-monitor', text)
        self.assertIn('description:', text)

    def test_douyin_scripts_compile(self):
        scripts = list((BOT / 'skills' / 'douyin-comments' / 'scripts').glob('*.py'))
        self.assertTrue(scripts, 'no Douyin scripts found')
        for path in scripts:
            py_compile.compile(str(path), doraise=True)

    def test_no_legacy_modules(self):
        self.assertFalse((ROOT / 'lib' / 'aisa').exists(), 'lib/aisa should be gone')
        self.assertFalse((ROOT / 'bots' / 'newterm').exists(), 'newterm should be gone')
        self.assertFalse((ROOT / 'bots' / 'site-ops').exists(), 'site-ops should be gone')
        self.assertFalse((ROOT / 'bots' / 'social-kb').exists(), 'social-kb should be gone')


class RunLog(unittest.TestCase):
    S = 'lib/runlog/runlog.py'

    def rl(self, d, *args):
        env = dict(os.environ, RUNLOG_HOME=str(d))
        return subprocess.run([sys.executable, str(ROOT / self.S), *args],
                              capture_output=True, text=True, env=env, cwd=ROOT)

    def test_start_end(self):
        with tempfile.TemporaryDirectory() as d:
            start = self.rl(d, 'start', '早报')
            self.assertEqual(start.returncode, 0, start.stderr)
            rid = start.stdout.strip()
            self.assertTrue(rid)
            end = self.rl(d, 'end', rid, '--status', 'ok', '--outputs', '5', '--pushed')
            self.assertEqual(end.returncode, 0, end.stderr)
            rows = [json.loads(line) for line in Path(d, 'runs.jsonl').read_text().splitlines()]
            self.assertEqual(rows[-1]['status'], 'ok')
            self.assertEqual(rows[-1]['outputs'], 5)
            self.assertTrue(rows[-1].get('pushed'))

    def test_approval_and_rule_change(self):
        with tempfile.TemporaryDirectory() as d:
            rc = self.rl(d, 'approve', '--kind', 'spend', '--ask', '投放预算', '--answer', 'yes', '--run', 'r-test')
            self.assertEqual(rc.returncode, 0, rc.stderr)
            rc = self.rl(d, 'rule', '--what', 'x.md', '--why', '测试规则变更')
            self.assertEqual(rc.returncode, 0, rc.stderr)
            self.assertTrue(Path(d, 'approvals.jsonl').is_file())
            self.assertTrue(Path(d, 'rules-changelog.md').is_file())


if __name__ == '__main__':
    unittest.main(verbosity=2)
