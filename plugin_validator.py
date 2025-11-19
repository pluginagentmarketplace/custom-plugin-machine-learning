#!/usr/bin/env python3
"""
Comprehensive plugin validator and integration checker.
Ensures all components are properly integrated and production-ready.
"""

import os
import json
from pathlib import Path

class PluginValidator:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.successes = []
        self.plugin_dir = Path('.')

    def validate_all(self):
        """Run all validations"""
        print("\n🔍 COMPREHENSIVE PLUGIN VALIDATION\n" + "="*50)

        self.validate_plugin_json()
        self.validate_agents()
        self.validate_skills()
        self.validate_commands()
        self.validate_hooks()
        self.validate_documentation()
        self.validate_integration()

        self.print_report()

    def validate_plugin_json(self):
        """Validate plugin.json structure"""
        print("\n📋 Validating plugin.json...")
        try:
            with open('.claude-plugin/plugin.json', 'r') as f:
                data = json.load(f)

            # Check required fields
            required = ['name', 'version', 'description', 'author', 'agents', 'skills', 'commands']
            for field in required:
                if field not in data:
                    self.errors.append(f"plugin.json missing required field: {field}")
                else:
                    self.successes.append(f"✅ plugin.json field '{field}' present")

            # Check counts
            self.successes.append(f"✅ {len(data['agents'])} agents defined")
            self.successes.append(f"✅ {len(data['skills'])} skills defined")
            self.successes.append(f"✅ {len(data['commands'])} commands defined")

            if len(data['agents']) < 5:
                self.warnings.append(f"⚠️  Only {len(data['agents'])} agents (recommend 8+)")
            if len(data['skills']) < 20:
                self.warnings.append(f"⚠️  Only {len(data['skills'])} skills (recommend 50+)")

        except Exception as e:
            self.errors.append(f"Error reading plugin.json: {str(e)}")

    def validate_agents(self):
        """Validate all agents"""
        print("\n🤖 Validating agents...")
        try:
            with open('.claude-plugin/plugin.json', 'r') as f:
                data = json.load(f)

            agent_ids = []
            for agent in data['agents']:
                agent_id = agent.get('id')
                agent_file = agent.get('file')

                if not agent_id or not agent_file:
                    self.errors.append(f"Agent missing id or file reference")
                    continue

                agent_ids.append(agent_id)

                # Check if file exists
                if not Path(agent_file).exists():
                    self.errors.append(f"Agent file not found: {agent_file}")
                else:
                    # Validate file content
                    with open(agent_file, 'r') as f:
                        content = f.read()
                        if '---' in content and '# ' in content:
                            self.successes.append(f"✅ Agent {agent_id} valid")
                        else:
                            self.errors.append(f"Agent {agent_id} missing frontmatter or title")

            self.successes.append(f"✅ All {len(agent_ids)} agents have proper structure")

        except Exception as e:
            self.errors.append(f"Error validating agents: {str(e)}")

    def validate_skills(self):
        """Validate all skills"""
        print("\n💡 Validating skills...")
        try:
            with open('.claude-plugin/plugin.json', 'r') as f:
                data = json.load(f)

            skill_count = 0
            for skill in data['skills']:
                skill_id = skill.get('id')
                skill_file = skill.get('file')

                if not skill_id or not skill_file:
                    continue

                if Path(skill_file).exists():
                    skill_count += 1
                else:
                    self.warnings.append(f"⚠️  Skill file not found: {skill_file}")

            self.successes.append(f"✅ {skill_count} skill files validated")

        except Exception as e:
            self.errors.append(f"Error validating skills: {str(e)}")

    def validate_commands(self):
        """Validate all commands"""
        print("\n⌨️  Validating commands...")
        try:
            with open('.claude-plugin/plugin.json', 'r') as f:
                data = json.load(f)

            command_count = 0
            for cmd in data['commands']:
                cmd_name = cmd.get('name')
                cmd_file = cmd.get('file')

                if Path(cmd_file).exists():
                    command_count += 1
                else:
                    self.errors.append(f"Command file not found: {cmd_file}")

            self.successes.append(f"✅ {command_count} command files validated")

        except Exception as e:
            self.errors.append(f"Error validating commands: {str(e)}")

    def validate_hooks(self):
        """Validate hooks"""
        print("\n🪝 Validating hooks...")
        try:
            if Path('hooks/hooks.json').exists():
                with open('hooks/hooks.json', 'r') as f:
                    data = json.load(f)
                self.successes.append(f"✅ hooks.json is valid JSON")
            else:
                self.warnings.append("⚠️  hooks.json not found")

            # Check hook implementations
            hooks = ['on-load.js', 'on-skill-invoke.js']
            for hook in hooks:
                if Path(f'hooks/{hook}').exists():
                    self.successes.append(f"✅ Hook {hook} found")
                else:
                    self.warnings.append(f"⚠️  Hook {hook} not found")

        except Exception as e:
            self.errors.append(f"Error validating hooks: {str(e)}")

    def validate_documentation(self):
        """Validate documentation"""
        print("\n📚 Validating documentation...")
        docs = ['README.md', 'CHANGELOG.md', 'INTEGRATION.md', 'QUALITY_STANDARDS.md', 'LICENSE']

        for doc in docs:
            if Path(doc).exists():
                self.successes.append(f"✅ {doc} present")
            else:
                self.warnings.append(f"⚠️  {doc} missing")

    def validate_integration(self):
        """Validate component integration"""
        print("\n🔗 Validating integration...")
        try:
            with open('.claude-plugin/plugin.json', 'r') as f:
                data = json.load(f)

            # Check agent-skill mapping
            skill_agents = set()
            for skill in data['skills']:
                agent = skill.get('agent')
                if agent:
                    skill_agents.add(agent)

            agent_ids = {a['id'] for a in data['agents']}
            unmapped = skill_agents - agent_ids

            if unmapped:
                self.errors.append(f"Skills reference non-existent agents: {unmapped}")
            else:
                self.successes.append(f"✅ All skill-agent mappings valid")

            # Check for duplicate IDs
            agent_ids = [a['id'] for a in data['agents']]
            if len(agent_ids) != len(set(agent_ids)):
                self.errors.append("Duplicate agent IDs found")

            skill_ids = [s['id'] for s in data['skills']]
            if len(skill_ids) != len(set(skill_ids)):
                self.errors.append("Duplicate skill IDs found")
            else:
                self.successes.append(f"✅ No duplicate IDs")

        except Exception as e:
            self.errors.append(f"Error validating integration: {str(e)}")

    def print_report(self):
        """Print validation report"""
        print("\n" + "="*50)
        print("VALIDATION REPORT")
        print("="*50)

        if self.successes:
            print("\n✅ PASSED VALIDATIONS:")
            for success in self.successes[:10]:  # Show first 10
                print(f"   {success}")
            if len(self.successes) > 10:
                print(f"   ... and {len(self.successes) - 10} more")

        if self.warnings:
            print("\n⚠️  WARNINGS:")
            for warning in self.warnings:
                print(f"   {warning}")

        if self.errors:
            print("\n❌ ERRORS:")
            for error in self.errors:
                print(f"   {error}")

        # Summary
        print("\n" + "="*50)
        print(f"📊 SUMMARY")
        print(f"   Successes: {len(self.successes)}")
        print(f"   Warnings: {len(self.warnings)}")
        print(f"   Errors: {len(self.errors)}")

        if self.errors == 0:
            print(f"\n✅ PLUGIN IS PRODUCTION READY!")
        elif self.errors:
            print(f"\n⚠️  PLUGIN HAS {len(self.errors)} CRITICAL ERRORS")

        print("="*50)

if __name__ == "__main__":
    validator = PluginValidator()
    validator.validate_all()
