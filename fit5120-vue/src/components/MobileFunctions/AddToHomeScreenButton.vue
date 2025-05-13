<template>
  <div v-if="deferredPrompt && !installed" class="add-to-home">
    <button @click="promptInstall">📲 Add to Home Screen</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const deferredPrompt = ref(null)
const installed = ref(false)

onMounted(() => {
  // 
  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault()
    deferredPrompt.value = e
  })

  // 
  window.addEventListener('appinstalled', () => {
    installed.value = true
  })
})

const promptInstall = async () => {
  if (deferredPrompt.value) {
    deferredPrompt.value.prompt()
    const { outcome } = await deferredPrompt.value.userChoice
    if (outcome === 'accepted') {
      console.log('User accepted install prompt')
    } else {
      console.log('User dismissed install prompt')
    }
    deferredPrompt.value = null
  }
}
</script>

<style scoped>
.add-to-home {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #4CAF50;
  padding: 10px 20px;
  border-radius: 50px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.2);
}

.add-to-home button {
  border: none;
  background: none;
  color: white;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
}
</style>
