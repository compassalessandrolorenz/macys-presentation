<template>
  <div class="min-h-screen flex flex-col">
    <Header />
    <main class="flex-grow py-8 bg-gray-100">
      <router-view />
    </main>
    <Footer />
  </div>
</template>

<script>
import Header from './components/Header/Header.vue';
import Footer from './components/Footer/Footer.vue';

export default {
  name: 'App',
  components: {
    Header,
    Footer
  }
}
</script>
