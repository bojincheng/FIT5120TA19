<template>
  <div class="beach-nav-container">
    <!-- Top Navigation Bar -->
    <nav class="top-nav">
      <router-link to="/home" class="nav-brand">WaterWiseFamily</router-link>
      
      <div class="nav-links">
        <router-link to="/beach-safety" class="nav-link">Australian Beach Conditions</router-link>
        <div class="nav-dropdown">
          <router-link to="/beach-safety-practices" class="nav-link dropdown-toggle">
            Preventing Risk
            <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </router-link>
          <div class="dropdown-menu">
            <router-link to="/beach-safety-practices" class="dropdown-item">Picking the Right Spot</router-link>
            <router-link to="/understanding-danger" class="dropdown-item">Understanding Rip Currents</router-link>
            <router-link to="/spot-rip-currents" class="dropdown-item">Avoiding Rip Currents</router-link>
          </div>
        </div>
        <div class="nav-dropdown">
          <router-link to="/beach-safety-rescue" class="nav-link dropdown-toggle">
            Facing the Risk
            <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </router-link>
          <div class="dropdown-menu">
            <router-link to="/beach-safety-rescue" class="dropdown-item">Signs of Trouble</router-link>
            <router-link to="/survive-rip-currents" class="dropdown-item">Survive Rip Currents</router-link>
            <router-link to="/safety-tool" class="dropdown-item">Safety Tools</router-link>
          </div>
        </div>
        <router-link to="/our-mission" class="nav-link">Our Mission</router-link>
      </div>
      
      <div class="safety-mode-selector">
        <div class="selected-mode" @click="toggleModeDropdown">
          <span>{{ safetyMode }}</span>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </div>
        <div class="mode-dropdown" v-show="modeDropdownOpen">
          <div class="mode-option" @click="selectMode('Beach Safety')" :class="{ active: safetyMode === 'Beach Safety' }">Beach Safety</div>
          <div class="mode-option" @click="selectMode('Pool Safety')" :class="{ active: safetyMode === 'Pool Safety' }">Pool Safety</div>
        </div>
      </div>
    </nav>
    
    <!-- Mobile Menu Toggle Button -->
    <div class="mobile-toggle" @click="toggleMenu">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
    </div>
    
    <!-- Mobile Menu Overlay -->
    <div class="mobile-overlay" v-if="menuOpen" @click="toggleMenu"></div>
    
    <!-- Mobile Menu -->
    <div class="mobile-menu" :class="{ 'open': menuOpen }">
      <div class="mobile-menu-header">
        <router-link to="/home" class="brand-logo">WaterWiseFamily</router-link>
        <div class="close-menu" @click="toggleMenu">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </div>
      </div>
      
      <div class="mobile-mode-selector">
        <div class="mobile-mode-label">Safety Mode:</div>
        <div class="mobile-mode-options">
          <div class="mobile-mode-option" 
               @click="selectMode('Beach Safety')" 
               :class="{ active: safetyMode === 'Beach Safety' }">
            Beach Safety
          </div>
          <div class="mobile-mode-option" 
               @click="selectMode('Pool Safety')" 
               :class="{ active: safetyMode === 'Pool Safety' }">
            Pool Safety
          </div>
        </div>
      </div>
      
      <div class="mobile-nav-links">
        <router-link to="/beach-safety" class="mobile-nav-link">Australian Beach Conditions</router-link>
        <div class="mobile-nav-dropdown">
          <div class="mobile-nav-link dropdown-toggle" @click="toggleMobilePreventingDropdown">
            Preventing Risk
            <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </div>
          <div class="mobile-dropdown-menu" v-show="mobilePreventingDropdownOpen">
            <router-link to="/beach-safety-practices" class="mobile-dropdown-item">Picking the Right Spot</router-link>
            <router-link to="/understanding-danger" class="mobile-dropdown-item">Understanding Rip Currents</router-link>
            <router-link to="/spot-rip-currents" class="mobile-dropdown-item">Avoiding Rip Currents</router-link>
          </div>
        </div>
        <div class="mobile-nav-dropdown">
          <div class="mobile-nav-link dropdown-toggle" @click="toggleMobileDropdown">
            Facing the Risk
            <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </div>
          <div class="mobile-dropdown-menu" v-show="mobileDropdownOpen">
            <router-link to="/beach-safety-rescue" class="mobile-dropdown-item">Signs of Trouble</router-link>
            <router-link to="/survive-rip-currents" class="mobile-dropdown-item">Survive Rip Currents</router-link>
            <router-link to="/safety-tool" class="mobile-dropdown-item">Safety Tools</router-link>
          </div>
        </div>
        <router-link to="/our-mission" class="mobile-nav-link">Our Mission</router-link>
      </div>
      
      <div class="mobile-safety-tip">
        <div class="tip-icon">💡</div>
        <div class="tip-text">Always swim between the red and yellow flags at patrolled beaches.</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BeachMenu',
  props: {
    menuOpen: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      modeDropdownOpen: false,
      mobileDropdownOpen: false,
      mobilePreventingDropdownOpen: false,
      safetyMode: 'Beach Safety'
    }
  },
  mounted() {
    // Close dropdown when clicking outside
    document.addEventListener('click', this.closeDropdownOutside);
  },
  beforeDestroy() {
    document.removeEventListener('click', this.closeDropdownOutside);
  },
  methods: {
    toggleMenu() {
      this.$emit('toggle-menu');
    },
    toggleModeDropdown(event) {
      // Stop propagation to prevent document click handler from immediately closing it
      event.stopPropagation();
      this.modeDropdownOpen = !this.modeDropdownOpen;
    },
    toggleMobileDropdown(event) {
      event.stopPropagation();
      this.mobileDropdownOpen = !this.mobileDropdownOpen;
    },
    toggleMobilePreventingDropdown(event) {
      event.stopPropagation();
      this.mobilePreventingDropdownOpen = !this.mobilePreventingDropdownOpen;
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
      const navDropdown = document.querySelector('.nav-dropdown');
      
      if (selector && !selector.contains(event.target)) {
        this.modeDropdownOpen = false;
      }
      
      if (navDropdown && !navDropdown.contains(event.target)) {
        // Close any other dropdowns if needed
      }
    }
  }
}
</script>

<style scoped>
/* Top Navigation Bar Styles */
.beach-nav-container {
  position: relative;
  width: 100%;
  z-index: 15;
}

.top-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.8rem 2rem;
  background: rgba(1, 54, 92, 0.85);
  backdrop-filter: blur(8px);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
  border-bottom: 2px solid rgba(243, 156, 18, 0.3);
}

.nav-brand {
  font-size: 1.6rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #ffffff;
  text-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  text-decoration: none;
  transition: all 0.2s ease;
}

.nav-brand:hover {
  color: #f39c12;
  transform: translateY(-1px);
}

.nav-links {
  display: flex;
  gap: 1.5rem;
  align-items: center;
}

.nav-link {
  color: rgba(255, 255, 255, 0.85);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.95rem;
  padding: 0.5rem 0;
  position: relative;
  transition: all 0.2s ease;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: #f39c12;
  transition: width 0.2s ease;
}

.nav-link:hover {
  color: #ffffff;
}

.nav-link:hover::after {
  width: 100%;
}

.nav-link.active {
  color: #f39c12;
}

.nav-link.active::after {
  width: 100%;
  background: #f39c12;
}

.safety-mode-selector {
  position: relative;
}

.selected-mode {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(243, 156, 18, 0.3);
  padding: 0.4rem 1rem;
  border-radius: 2rem;
  border: 1px solid rgba(243, 156, 18, 0.5);
  cursor: pointer;
  transition: all 0.2s ease;
}

.selected-mode:hover {
  background: rgba(243, 156, 18, 0.4);
  transform: translateY(-2px);
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.15);
}

.selected-mode span {
  font-weight: 700;
  font-size: 0.95rem;
  color: white;
}

.selected-mode svg {
  color: white;
  transition: transform 0.3s ease;
}

.selected-mode:hover svg {
  transform: translateY(2px);
}

.mode-dropdown {
  position: absolute;
  top: calc(100% + 8px);
  right: 0;
  background: rgba(1, 54, 92, 0.95);
  border-radius: 0.75rem;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
  padding: 0.5rem;
  z-index: 10;
  min-width: 160px;
  border: 1px solid rgba(243, 156, 18, 0.3);
  animation: fadeDown 0.2s ease-out;
}

@keyframes fadeDown {
  from { 
    opacity: 0;
    transform: translateY(-10px);
  }
  to { 
    opacity: 1;
    transform: translateY(0);
  }
}

.mode-option {
  padding: 0.75rem 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
  color: rgba(255, 255, 255, 0.85);
  border-radius: 0.5rem;
  font-weight: 500;
  display: flex;
  align-items: center;
}

.mode-option:before {
  content: "";
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: transparent;
  margin-right: 8px;
  border: 1px solid rgba(243, 156, 18, 0.5);
  transition: all 0.2s ease;
}

.mode-option:hover {
  background: rgba(243, 156, 18, 0.2);
  color: white;
}

.mode-option.active {
  background: rgba(243, 156, 18, 0.3);
  color: white;
}

.mode-option.active:before {
  background: #f39c12;
  box-shadow: 0 0 5px rgba(243, 156, 18, 0.5);
}

/* Mobile Menu Styles */
.mobile-toggle {
  display: none;
  position: absolute;
  right: 1.5rem;
  top: 1.2rem;
  align-items: center;
  justify-content: center;
  color: white;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  width: 40px;
  height: 40px;
  cursor: pointer;
  transition: all 0.3s ease;
  z-index: 15;
}

.mobile-toggle:hover {
  background: rgba(255, 255, 255, 0.3);
}

.mobile-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  z-index: 48;
  backdrop-filter: blur(3px);
  transition: all 0.3s ease;
}

.mobile-menu {
  position: fixed;
  top: 0;
  right: -300px;
  width: 280px;
  height: 100%;
  background: linear-gradient(165deg, #01365c, #012a47);
  z-index: 49;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
  transition: right 0.3s ease;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

.mobile-menu.open {
  right: 0;
}

.mobile-menu-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.brand-logo {
  font-size: 1.4rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #ffffff;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
  text-decoration: none;
  transition: all 0.2s ease;
}

.brand-logo:hover {
  color: #f39c12;
}

.close-menu {
  cursor: pointer;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.close-menu:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: rotate(90deg);
}

.mobile-mode-selector {
  margin: 0.5rem 1.5rem 1rem;
  padding: 1rem;
  border-radius: 0.75rem;
  background: rgba(243, 156, 18, 0.15);
  border: 1px solid rgba(243, 156, 18, 0.3);
}

.mobile-mode-label {
  font-weight: 600;
  color: white;
  margin-bottom: 0.5rem;
}

.mobile-mode-options {
  display: flex;
  gap: 0.5rem;
  background: rgba(1, 54, 92, 0.5);
  padding: 0.25rem;
  border-radius: 0.5rem;
}

.mobile-mode-option {
  flex: 1;
  padding: 0.6rem 1rem;
  border-radius: 0.35rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s ease;
  color: rgba(255, 255, 255, 0.8);
  font-weight: 500;
}

.mobile-mode-option:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.mobile-mode-option.active {
  background: rgba(243, 156, 18, 0.35);
  color: white;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

.mobile-nav-links {
  display: flex;
  flex-direction: column;
  padding: 1rem 0;
}

.mobile-nav-link {
  display: block;
  padding: 1rem 1.5rem;
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  border-left: 3px solid transparent;
  font-weight: 500;
  transition: all 0.2s ease;
}

.mobile-nav-link:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
  border-left-color: #f39c12;
}

.mobile-nav-link.active {
  background: rgba(243, 156, 18, 0.15);
  color: #f39c12;
  border-left-color: #f39c12;
}

.mobile-safety-tip {
  margin-top: auto;
  padding: 1rem 1.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  gap: 0.8rem;
  align-items: flex-start;
}

.tip-icon {
  font-size: 1.5rem;
}

.tip-text {
  font-size: 0.9rem;
  line-height: 1.4;
  color: rgba(255, 255, 255, 0.9);
}

/* Responsive Styles */
@media (max-width: 1024px) {
  .nav-links {
    gap: 1rem;
  }
  
  .nav-link {
    font-size: 0.9rem;
  }
}

@media (max-width: 768px) {
  .top-nav {
    padding: 1rem;
  }
  
  .nav-brand {
    margin: 0 auto;
  }
  
  .nav-links, .safety-mode-selector {
    display: none;
  }
  
  .mobile-toggle {
    display: flex;
  }
}

@media (max-width: 480px) {
  .mobile-menu {
    width: 250px;
  }
  
  .mobile-nav-link {
    padding: 0.8rem 1.25rem;
  }
}

/* Add dropdown styles */
.nav-dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-toggle {
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.dropdown-menu {
  position: absolute;
  top: calc(100% + 10px);
  left: 50%;
  transform: translateX(-50%);
  background: rgba(1, 54, 92, 0.95);
  border-radius: 0.75rem;
  min-width: 200px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
  padding: 0.5rem;
  z-index: 100;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
  border: 1px solid rgba(243, 156, 18, 0.3);
}

.nav-dropdown:hover .dropdown-menu {
  opacity: 1;
  visibility: visible;
  top: calc(100% + 5px);
}

.dropdown-item {
  display: block;
  padding: 0.75rem 1rem;
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  border-radius: 0.5rem;
  transition: all 0.2s ease;
  font-weight: 500;
  text-align: left;
}

.dropdown-item:hover {
  background: rgba(243, 156, 18, 0.2);
  color: white;
}

.dropdown-item.active {
  color: #f39c12;
  background: rgba(243, 156, 18, 0.1);
}

/* Mobile dropdown styles */
.mobile-nav-dropdown {
  position: relative;
}

.mobile-nav-dropdown .dropdown-toggle {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.mobile-dropdown-menu {
  background: rgba(1, 54, 92, 0.5);
  margin: 0.25rem 0 0.25rem 1rem;
  border-left: 2px solid rgba(243, 156, 18, 0.5);
  border-radius: 0 0 0.5rem 0.5rem;
  overflow: hidden;
  animation: slideDown 0.3s ease;
}

@keyframes slideDown {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

.mobile-dropdown-item {
  display: block;
  padding: 0.75rem 1.5rem;
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  transition: all 0.2s ease;
  font-weight: 500;
  font-size: 0.9rem;
}

.mobile-dropdown-item:hover {
  background: rgba(243, 156, 18, 0.1);
  color: white;
}

.mobile-dropdown-item.active {
  color: #f39c12;
  background: rgba(243, 156, 18, 0.1);
}
</style> 