// Plugin initialization hook
module.exports = async (context) => {
  try {
    // Check user profile
    const user = context.getUserProfile();

    if (!user.previousSessions) {
      // First time user
      console.log("🎉 Welcome new user!");
      context.showWelcomeMessage();
    } else {
      // Returning user
      console.log(`📖 Welcome back, ${user.name}!`);
      context.suggestResume();
    }

    // Load learning history
    const history = context.getProgressHistory();
    console.log(`Progress: ${history.completed}/${history.total} skills`);

    // Check milestones
    const milestones = context.checkMilestones();
    if (milestones.length > 0) {
      milestones.forEach(m => context.awardBadge(m));
    }

    return { success: true, message: "Plugin loaded successfully" };
  } catch (error) {
    console.error("Error in onLoad hook:", error);
    return { success: false, error: error.message };
  }
};