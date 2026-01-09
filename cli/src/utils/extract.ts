import { cpSync, mkdirSync, existsSync, rmSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { AI_FOLDERS, AI_SKILL_PATH, type AIType } from '../types/index.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Assets are located relative to the compiled dist folder
function getAssetsDir(): string {
  // When running from dist/, go up to cli/, then into assets/
  return join(__dirname, '..', '..', 'assets');
}

export function extractSkill(targetDir: string, ai: Exclude<AIType, 'all'>, force = false): void {
  const assetsDir = getAssetsDir();
  const sourceSkillPath = join(assetsDir, AI_FOLDERS[ai], AI_SKILL_PATH);
  const targetSkillPath = join(targetDir, AI_FOLDERS[ai], AI_SKILL_PATH);

  if (!existsSync(sourceSkillPath)) {
    throw new Error(`Source skill not found: ${sourceSkillPath}`);
  }

  // Create parent directories if needed
  const targetParentDir = join(targetDir, AI_FOLDERS[ai], 'skills');
  if (!existsSync(targetParentDir)) {
    mkdirSync(targetParentDir, { recursive: true });
  }

  // Remove existing if force is true
  if (existsSync(targetSkillPath)) {
    if (!force) {
      throw new Error(`Skill already exists at ${targetSkillPath}. Use --force to overwrite.`);
    }
    rmSync(targetSkillPath, { recursive: true });
  }

  // Copy skill directory
  cpSync(sourceSkillPath, targetSkillPath, { recursive: true });
}

export function extractAll(targetDir: string, force = false): void {
  for (const ai of Object.keys(AI_FOLDERS) as Array<Exclude<AIType, 'all'>>) {
    extractSkill(targetDir, ai, force);
  }
}
