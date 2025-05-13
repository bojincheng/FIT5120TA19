<!-- src/components/MobileFunctions/AddToHomeScreenButton.vue -->
<template>
  <div v-if="showButton" class="install-banner">
    <button @click="triggerInstall">📲 Add to Home Screen</button>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const showButton = ref(false)
let deferredPrompt = null

const triggerInstall = async () => {
  if (!deferredPrompt) return
  deferredPrompt.prompt()
  const { outcome } = await deferredPrompt.userChoice
  if (outcome === 'accepted') {
    console.log('User accepted install prompt')
  } else {
    console.log('User dismissed install prompt')
  }
  deferredPrompt = null
  showButton.value = false
}

onMounted(() => {
  window.addEventListener('beforeinstallprompt', handleBeforeInstallPrompt)
  window.addEventListener('appinstalled', () => {
    console.log('App installed')
    showButton.value = false
  })
})

onBeforeUnmount(() => {
  window.removeEventListener('beforeinstallprompt', handleBeforeInstallPrompt)
})

const handleBeforeInstallPrompt = (e) => {
  e.preventDefault()
  deferredPrompt = e
  showButton.value = true
}
</script>

<style scoped>
.install-banner {
  position: fixed;
  bottom: 80px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #4CAF50;
  color: white;
  border-radius: 50px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.2);
  padding: 10px 20px;
  z-index: 1000;
}

.install-banner button {
  background: none;
  border: none;
  color: white;
  font-weight: bold;
  font-size: 16px;
  cursor: pointer;
}
</style>