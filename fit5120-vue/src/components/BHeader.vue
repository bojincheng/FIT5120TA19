<template>
    <div class="bottom-nav-container">
      <!-- Main navigation bar that stays fixed at the bottom of the screen -->
      <nav class="bottom-nav">
        <!-- Home navigation item -->
        <router-link to="/" class="nav-item" active-class="active">
          <div class="nav-icon">🏠</div>
          <div class="nav-label">Home</div>
        </router-link>
        <router-link to="/Drowningsearch" class="nav-item" active-class="active">
          <div class="nav-icon">🏠</div>
          <div class="nav-label">Drowningsearch</div>
        </router-link>
        
      </nav>
    </div>
  </template>