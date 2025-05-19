<template>
  <div class="app-wrapper">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>body {  margin: 0;  padding: 0;  font-family: Arial, sans-serif;  overflow-x: hidden;  width: 100%;  box-sizing: border-box;}html {  font-size: 16px;  -webkit-text-size-adjust: 100%;}*, *::before, *::after {  box-sizing: border-box;}img {  max-width: 100%;  height: auto;}.app-wrapper {  position: relative;  min-height: 100vh;  width: 100%;  overflow-x: hidden;}@media screen and (min-width: 1200px) {  .app-wrapper {    max-width: 100%;    margin: 0 auto;  }}@media (forced-colors: active) {  * {    forced-color-adjust: none;  }}</style>  