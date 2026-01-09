import { existsSync } from 'node:fs';
import { join } from 'node:path';
import { AI_FOLDERS, AI_SKILL_PATH, type AIType } from '../types/index.js';

export function detectAIFolders(targetDir: string): AIType[] {
  const detected: AIType[] = [];

  for (const [ai, folder] of Object.entries(AI_FOLDERS)) {
    const folderPath = join(targetDir, folder);
    if (existsSync(folderPath)) {
      detected.push(ai as AIType);
    }
  }

  return detected;
}

export function isSkillInstalled(targetDir: string, ai: Exclude<AIType, 'all'>): boolean {
  const skillPath = join(targetDir, AI_FOLDERS[ai], AI_SKILL_PATH);
  return existsSync(skillPath);
}

export function getSkillPath(targetDir: string, ai: Exclude<AIType, 'all'>): string {
  return join(targetDir, AI_FOLDERS[ai], AI_SKILL_PATH);
}
