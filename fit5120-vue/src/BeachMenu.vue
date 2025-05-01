<template>
  <!-- No changes to template section -->
</template>

<script>
export default {
  methods: {
    toggleMenu() {
      this.$emit('toggle-menu');
    },
    toggleModeDropdown(event) {
      // Stop propagation to prevent document click handler from immediately closing it
      event.stopPropagation();
      this.modeDropdownOpen = !this.modeDropdownOpen;
    },
    selectMode(mode) {
      this.safetyMode = mode;
      this.modeDropdownOpen = false;
      
      // Navigate to the appropriate page based on the selected mode
      if (mode === 'Beach Safety') {
        this.$router.push('/beach-safety');
      } else if (mode === 'Pool Safety') {
        this.$router.push('/pool-safety');
      }
      
      // Emit event for parent component to handle mode change
      this.$emit('mode-change', mode);
    },
    closeDropdownOutside(event) {
      const selector = document.querySelector('.safety-mode-selector');
      if (selector && !selector.contains(event.target)) {
        this.modeDropdownOpen = false;
      }
    }
  }
};
</script>

<style>
  /* No changes to style section */
</style> 