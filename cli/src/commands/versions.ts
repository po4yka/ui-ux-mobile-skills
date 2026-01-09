import type { VersionInfo } from '../types/index.js';
import { logger } from '../utils/logger.js';

const VERSIONS: VersionInfo[] = [
  {
    version: '1.0.0',
    date: '2026-01-09',
    changes: [
      'Initial release',
      'Support for Claude Code and OpenAI Codex',
      '8 search domains: style, color, typography, component, navigation, gesture, accessibility, animation',
      '7 stack guides: SwiftUI, Jetpack Compose, Flutter, React Native, KMP, Material 3, Liquid Glass',
      'BM25 search algorithm',
    ],
  },
];

export function versionsCommand(): void {
  logger.info('UI/UX Mobile Skill - Version History\n');

  for (const v of VERSIONS) {
    console.log(`v${v.version} (${v.date})`);
    for (const change of v.changes) {
      console.log(`  - ${change}`);
    }
    console.log('');
  }
}
