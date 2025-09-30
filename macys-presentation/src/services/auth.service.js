const API_URL = 'http://localhost:5000/api';

/**
 * Authentication service for handling user login/logout/registration
 */
class AuthService {
  /**
   * Register a new user
   * @param {string} name - User's name
   * @param {string} email - User's email
   * @param {string} password - User's password
   * @returns {Promise} - Promise with registration result
   */
  async register(name, email, password) {
    try {
      console.log(`Making API request to ${API_URL}/register with data:`, {
        name,
        email,
        password: '********' // Don't log actual password
      });
      
      const response = await fetch(`${API_URL}/register`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, email, password }),
      });

      console.log('API response status:', response.status);
      
      const data = await response.json();
      console.log('API response data:', data);
      
      return data;
    } catch (error) {
      console.error('Registration error details:', error);
      return {
        success: false,
        message: 'An error occurred during registration. Please try again.'
      };
    }
  }

  /**
   * Login user with email and password
   * @param {string} email - User email
   * @param {string} password - User password
   * @returns {Promise} - Promise with login result
   */
  async login(email, password) {
    try {
      const response = await fetch(`${API_URL}/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      const data = await response.json();
      
      if (data.success) {
        // Store user data in localStorage
        localStorage.setItem('user', JSON.stringify(data.user));
      }
      
      return data;
    } catch (error) {
      console.error('Login error:', error);
      return {
        success: false,
        message: 'An error occurred during login. Please try again.'
      };
    }
  }

  /**
   * Logout current user
   */
  logout() {
    localStorage.removeItem('user');
  }

  /**
   * Get current user data
   * @returns {Object|null} - User data or null if not logged in
   */
  getCurrentUser() {
    const userStr = localStorage.getItem('user');
    if (!userStr) return null;
    
    try {
      return JSON.parse(userStr);
    } catch (e) {
      return null;
    }
  }

  /**
   * Check if user is logged in
   * @returns {boolean} - True if user is logged in
   */
  isLoggedIn() {
    return this.getCurrentUser() !== null;
  }
}

export default new AuthService();
