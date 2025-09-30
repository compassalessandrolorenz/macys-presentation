<template>
  <header>
    <!-- Top strip with free shipping info -->
    <div class="bg-gray-100 text-sm text-center py-1">
      <span>Free shipping with $25 purchase or Find & Free Store Pickup. <a href="#" class="text-red-600 underline">Exclusions</a></span>
    </div>

    <!-- Main header with logo and navigation -->
    <div class="container-center py-2">
      <div class="flex justify-between items-center w-full">
        <!-- Logo -->
        <a href="#" class="text-2xl font-bold">
          <span class="text-red-600">★</span>macy's
        </a>

        <!-- Search, wishlist, cart, sign in -->
        <div class="flex items-center gap-4">
          <!-- Search box -->
          <div class="relative">
            <input type="text" placeholder="Search" class="bg-gray-100 border border-gray-300 rounded-md py-1 px-3 pr-8">
            <span class="absolute right-2 top-1/2 transform -translate-y-1/2">🔍</span>
          </div>
          
          <!-- Icons -->
          <a href="#" aria-label="Wishlist">❤</a>
          <a href="#" aria-label="Shopping bag">👜</a>
          <router-link 
            :to="isAuthenticated ? '/welcome' : '/signin'" 
            class="text-sm"
          >
            {{ isAuthenticated ? 'My Account' : 'Sign In' }}
          </router-link>
        </div>
      </div>
    </div>

    <!-- Navigation menu -->
    <nav class="border-t border-b border-gray-200">
      <div class="container-center">
        <ul class="flex text-sm overflow-x-auto py-2 gap-4 w-screen items-center justify-center">
          <li><a href="#" class="whitespace-nowrap">Women</a></li>
          <li><a href="#" class="whitespace-nowrap">Men</a></li>
          <li><a href="#" class="whitespace-nowrap">Beauty</a></li>
          <li><a href="#" class="whitespace-nowrap">Shoes</a></li>
          <li><a href="#" class="whitespace-nowrap">Home</a></li>
          <li><a href="#" class="whitespace-nowrap">Jewelry</a></li>
          <li><a href="#" class="whitespace-nowrap">Handbags</a></li>
          <li><a href="#" class="whitespace-nowrap">Furniture & Mattresses</a></li>
          <li><a href="#" class="whitespace-nowrap">Kids & Baby</a></li>
          <li><a href="#" class="whitespace-nowrap">Toys</a></li>
          <li><a href="#" class="whitespace-nowrap">Electronics</a></li>
          <li><a href="#" class="whitespace-nowrap">Gifts</a></li>
          <li><a href="#" class="whitespace-nowrap">New & Trending</a></li>
          <li><a href="#" class="whitespace-nowrap text-red-600">Sale</a></li>
          <li v-if="!isAuthenticated"><router-link to="/signup" class="whitespace-nowrap">Email Signup</router-link></li>
          <li v-if="!isAuthenticated"><router-link to="/register" class="whitespace-nowrap">Register</router-link></li>
          <li v-if="!isAuthenticated"><router-link to="/signin" class="whitespace-nowrap">Sign In</router-link></li>
          <li v-if="isAuthenticated"><router-link to="/welcome" class="whitespace-nowrap">My Account</router-link></li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script>
import AuthService from '../../services/auth.service';

export default {
  name: 'Header',
  data() {
    return {
      isAuthenticated: false
    }
  },
  created() {
    // Check if user is authenticated
    this.checkAuthStatus();
    // Listen for storage events (for when user logs in/out in another tab)
    window.addEventListener('storage', this.checkAuthStatus);
  },
  unmounted() {
    // Remove event listener
    window.removeEventListener('storage', this.checkAuthStatus);
  },
  methods: {
    checkAuthStatus() {
      this.isAuthenticated = AuthService.isLoggedIn();
    }
  }
}
</script>
