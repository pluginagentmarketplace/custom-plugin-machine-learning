// Skill invocation hook
module.exports = async (context) => {
  try {
    const skillId = context.getSkillId();
    const skill = context.getSkill(skillId);

    // Track usage
    context.logEvent("skill_accessed", {
      skillId: skillId,
      skillName: skill.name,
      timestamp: new Date().toISOString()
    });

    // Update progress
    context.updateSkillProgress(skillId, "in_progress");

    // Suggest related content
    const related = context.getRelatedSkills(skillId);
    context.suggestRelated(related);

    // Check if completed
    if (context.isSkillComplete(skillId)) {
      context.markSkillComplete(skillId);
      context.awardPoints(100);
      context.checkNewMilestones();
    }

    return { success: true, skill: skill };
  } catch (error) {
    console.error("Error in onSkillInvoke hook:", error);
    return { success: false, error: error.message };
  }
};