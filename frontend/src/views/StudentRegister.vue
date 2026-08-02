<template>
  <div class="register-wrapper min-vh-100 d-flex justify-content-center align-items-center py-5">
    <div class="container py-3">
      <div class="row justify-content-center">
        <div class="col-12 col-md-10 col-lg-7 col-xl-6">

          <div class="card border-0 shadow-lg rounded-4 overflow-hidden">
            <!-- Header Accent Bar -->
            <div class="bg-primary py-1"></div>

            <div class="card-body p-4 p-sm-5">

              <!-- Header -->
              <div class="text-center mb-4">
                <div class="brand-badge bg-primary-subtle text-primary mb-3 mx-auto">
                  <i class="bi bi-person-badge-fill fs-3"></i>
                </div>
                <h2 class="fw-bold text-dark h3 mb-1">Student Registration</h2>
                <p class="text-secondary small mb-0">
                  Create your student profile to apply for placement drives
                </p>
              </div>

              <form @submit.prevent="registerStudent">

                <!-- Full Name & Email -->
                <div class="row g-3 mb-3">
                  <div class="col-12 col-md-6">
                    <label class="form-label fw-semibold text-secondary small">Full Name</label>
                    <div class="input-group">
                      <span class="input-group-text bg-light border-end-0 text-muted">
                        <i class="bi bi-person"></i>
                      </span>
                      <input
                        v-model="form.full_name"
                        type="text"
                        class="form-control bg-light border-start-0 ps-0"
                        placeholder="John Doe"
                        required
                      >
                    </div>
                  </div>

                  <div class="col-12 col-md-6">
                    <label class="form-label fw-semibold text-secondary small">Email Address</label>
                    <div class="input-group">
                      <span class="input-group-text bg-light border-end-0 text-muted">
                        <i class="bi bi-envelope"></i>
                      </span>
                      <input
                        v-model="form.email"
                        type="email"
                        class="form-control bg-light border-start-0 ps-0"
                        placeholder="student@example.com"
                        required
                      >
                    </div>
                  </div>
                </div>

                <!-- Password & Phone -->
                <div class="row g-3 mb-3">
                  <div class="col-12 col-md-6">
                    <label class="form-label fw-semibold text-secondary small">Password</label>
                    <div class="input-group">
                      <span class="input-group-text bg-light border-end-0 text-muted">
                        <i class="bi bi-lock"></i>
                      </span>
                      <input
                        v-model="form.password"
                        type="password"
                        class="form-control bg-light border-start-0 ps-0"
                        placeholder="••••••••"
                        required
                      >
                    </div>
                  </div>

                  <div class="col-12 col-md-6">
                    <label class="form-label fw-semibold text-secondary small">Phone Number</label>
                    <div class="input-group">
                      <span class="input-group-text bg-light border-end-0 text-muted">
                        <i class="bi bi-telephone"></i>
                      </span>
                      <input
                        v-model="form.phone"
                        type="text"
                        class="form-control bg-light border-start-0 ps-0"
                        placeholder="+91 9876543210"
                        required
                      >
                    </div>
                  </div>
                </div>

                <!-- Branch, CGPA & Passing Year -->
                <div class="row g-3 mb-3">
                  <div class="col-12 col-md-5">
                    <label class="form-label fw-semibold text-secondary small">Branch</label>
                    <div class="input-group">
                      <span class="input-group-text bg-light border-end-0 text-muted">
                        <i class="bi bi-journal-bookmark"></i>
                      </span>
                      <input
                        v-model="form.branch"
                        type="text"
                        class="form-control bg-light border-start-0 ps-0"
                        placeholder="e.g. CSE, Data Science"
                        required
                      >
                    </div>
                  </div>

                  <div class="col-6 col-md-3">
                    <label class="form-label fw-semibold text-secondary small">CGPA</label>
                    <div class="input-group">
                      <span class="input-group-text bg-light border-end-0 text-muted">
                        <i class="bi bi-award"></i>
                      </span>
                      <input
                        v-model="form.cgpa"
                        type="number"
                        step="0.01"
                        class="form-control bg-light border-start-0 ps-0"
                        placeholder="8.5"
                        required
                      >
                    </div>
                  </div>

                  <div class="col-6 col-md-4">
                    <label class="form-label fw-semibold text-secondary small">Passing Year</label>
                    <div class="input-group">
                      <span class="input-group-text bg-light border-end-0 text-muted">
                        <i class="bi bi-calendar-event"></i>
                      </span>
                      <input
                        v-model="form.passing_year"
                        type="number"
                        class="form-control bg-light border-start-0 ps-0"
                        placeholder="2026"
                        required
                      >
                    </div>
                  </div>
                </div>

                <!-- Skills -->
                <div class="mb-4">
                  <label class="form-label fw-semibold text-secondary small">Technical Skills</label>
                  <div class="input-group">
                    <span class="input-group-text bg-light border-end-0 text-muted align-items-start pt-2">
                      <i class="bi bi-code-slash"></i>
                    </span>
                    <textarea
                      v-model="form.skills"
                      class="form-control bg-light border-start-0 ps-0"
                      rows="3"
                      placeholder="Python, SQL, Java, Vue.js"
                      required
                    ></textarea>
                  </div>
                </div>

                <!-- Action Buttons -->
                <button
                  type="submit"
                  class="btn btn-primary w-100 py-2-5 mb-2 fw-semibold rounded-3 shadow-sm"
                >
                  <i class="bi bi-check-circle me-1"></i> Register
                </button>

                <button
                  type="button"
                  class="btn btn-outline-secondary w-100 py-2 fw-medium rounded-3"
                  @click="router.push('/login')"
                >
                  <i class="bi bi-arrow-left me-1"></i> Back to Login
                </button>

              </form>

            </div>
          </div>

          <!-- Bottom Branding -->
          <p class="text-center text-secondary small mt-4 mb-0">
            © 2026 Placement Portal • IIT Madras BS Degree
          </p>

        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from "vue";
import { useRouter } from "vue-router";
import api from "../services/api";

const router = useRouter();

const form = reactive({
  full_name: "",
  email: "",
  password: "",
  phone: "",
  branch: "",
  cgpa: "",
  passing_year: "",
  skills: ""
});

async function registerStudent() {
  try {
    const response = await api.post(
      "/student/register",
      form
    );

    alert(response.data.message);

    router.push("/login");

  } catch (error) {

    alert(
      error.response?.data?.message ||
      "Registration failed"
    );

  }
}
</script>

<style scoped>
.register-wrapper {
  background: radial-gradient(circle at 50% 10%, rgba(37, 99, 235, 0.08) 0%, rgba(248, 250, 252, 1) 70%);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

.brand-badge {
  width: 56px;
  height: 56px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.input-group-text {
  border-color: #dee2e6;
}

.form-control {
  border-color: #dee2e6;
  font-size: 0.95rem;
}

.form-control:focus {
  background-color: #ffffff !important;
  box-shadow: none;
  border-color: #2563eb;
}

.input-group:focus-within .input-group-text {
  background-color: #ffffff !important;
  border-color: #2563eb;
  color: #2563eb !important;
}

.py-2-5 {
  padding-top: 0.65rem;
  padding-bottom: 0.65rem;
}
</style>