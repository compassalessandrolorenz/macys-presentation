<template>
  <div class="container-center">
    <div class="bg-white p-6 mb-4 shadow-sm max-w-md w-full">
      <h1 class="text-2xl font-bold text-red-600 text-center uppercase mb-2">
        Welcome, {{ user ? user.name : 'User' }}!
      </h1>
      <p class="text-center text-sm mb-6">
        You have successfully signed in to your account.
      </p>
      
      <div class="flex justify-center">
        <button 
          @click="logout" 
          class="btn btn-primary"
        >
          Logout
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import AuthService from '../services/auth.service';

export default {
  name: 'WelcomePage',
  data() {
    return {
      user: null
    }
  },
  created() {
    // Get user data from auth service
    this.user = AuthService.getCurrentUser();
    
    // If no user data found, redirect to login
    if (!this.user) {
      this.$router.push('/signin');
    }
  },
  methods: {
    logout() {
      // Use auth service to logout
      AuthService.logout();
      // Redirect to login page
      this.$router.push('/signin');
    }
  }
}
</script>
