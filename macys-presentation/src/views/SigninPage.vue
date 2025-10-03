<template>
  <div class="container-center">
    <div class="bg-white p-6 mb-4 shadow-sm max-w-md w-full">
      <h1 class="text-2xl font-bold text-red-600 text-center uppercase mb-2">
        Sign in to your account
      </h1>
      <p class="text-center text-sm mb-6">
        Enter your credentials to access your account
      </p>

      <form @submit.prevent="login">
        <!-- Email input -->
        <div class="mb-4">
          <label for="email" class="block text-sm mb-1">email*</label>
          <input 
            type="email" 
            id="email" 
            v-model="email" 
            placeholder="Enter your email address" 
            class="input-field"
            required
          >
        </div>

        <!-- Password input -->
        <div class="mb-6">
          <label for="password" class="block text-sm mb-1">password*</label>
          <input 
            type="password" 
            id="password" 
            v-model="password" 
            placeholder="Enter your password" 
            class="input-field"
            required
          >
        </div>

        <!-- Error message -->
        <div v-if="errorMessage" class="mb-4 p-2 bg-red-100 text-red-700 text-sm rounded">
          {{ errorMessage }}
        </div>

        <!-- Submit button -->
        <button 
          type="submit" 
          class="btn btn-primary w-full" 
          :disabled="isLoading"
          :class="{ 'opacity-50 cursor-not-allowed': isLoading }"
        >
          {{ isLoading ? 'Signing in...' : 'Sign In' }}
        </button>
      </form>

      <div class="mt-4 text-center text-sm">
        <p>Don't have an account? <a href="/register" class="text-red-600">Register</a></p>
      </div>
    </div>
  </div>
</template>

<script>
import AuthService from '../services/auth.service';

export default {
  name: 'SigninPage',
  data() {
    return {
      email: '',
      password: '',
      errorMessage: '',
      isLoading: false
    }
  },
  created() {
    // If user is already logged in, redirect to welcome page
    if (AuthService.isLoggedIn()) {
      this.$router.push('/welcome');
    }
  },
  methods: {
    async login() {
      this.isLoading = true;
      this.errorMessage = '';
      
      try {
        const result = await AuthService.login(this.email, this.password);
        
        if (result.success) {
          // Redirect to welcome page
          this.$router.push('/welcome');
        } else {
          this.errorMessage = result.message || 'Failed to sign in. Please check your credentials.';
        }
      } catch (error) {
        this.errorMessage = 'An error occurred. Please try again.';
        console.error('Login error:', error);
      } finally {
        this.isLoading = false;
      }
    }
  }
}
</script>
