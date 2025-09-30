<template>
  <header class="bg-blue-800 text-white p-4">
    <h1 class="text-2xl font-bold">Macy's Presentation</h1>
  </header>
  
  <main class="container mx-auto p-4">
    <router-view />
  </main>
  
  <footer class="bg-gray-200 p-4 text-center">
    <p>&copy; 2023 Macy's Presentation</p>
  </footer>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
@import './assets/main.css';
</style>