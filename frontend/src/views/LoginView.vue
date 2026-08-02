<template>
  <div class="login-wrapper min-vh-100 d-flex justify-content-center align-items-center py-5">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-12 col-sm-10 col-md-8 col-lg-5 col-xl-4">
          
          <div class="card border-0 shadow-lg rounded-4 overflow-hidden">
            <!-- Header Accent Bar -->
            <div class="bg-primary py-1"></div>

            <div class="card-body p-4 p-sm-5">
              
              <!-- Brand Header -->
              <div class="text-center mb-4">
                <div class="brand-badge bg-primary-subtle text-primary mb-3 mx-auto">
                  <i class="bi bi-mortarboard-fill fs-3"></i>
                </div>
                <h2 class="fw-bold text-dark h3 mb-1">Placement Portal</h2>
                <p class="text-secondary small mb-0">
                  IIT Madras Placement Portal
                </p>
              </div>

              <!-- Form Inputs -->
              <div class="mb-3">
                <label class="form-label fw-semibold text-secondary small">Email Address</label>
                <div class="input-group">
                  <span class="input-group-text bg-light border-end-0 text-muted">
                    <i class="bi bi-envelope"></i>
                  </span>
                  <input
                    type="email"
                    class="form-control bg-light border-start-0 ps-0"
                    v-model="email"
                    placeholder="Enter email"
                  />
                </div>
              </div>

              <div class="mb-4">
                <label class="form-label fw-semibold text-secondary small">Password</label>
                <div class="input-group">
                  <span class="input-group-text bg-light border-end-0 text-muted">
                    <i class="bi bi-lock"></i>
                  </span>
                  <input
                    type="password"
                    class="form-control bg-light border-start-0 ps-0"
                    v-model="password"
                    placeholder="Enter password"
                  />
                </div>
              </div>

              <!-- Login Button -->
              <button
                class="btn btn-primary w-100 py-2-5 mb-4 fw-semibold rounded-3 shadow-sm"
                @click="login"
              >
                <i class="bi bi-box-arrow-in-right me-1"></i> Login
              </button>

              <!-- Divider -->
              <div class="position-relative text-center my-3">
                <hr class="text-secondary opacity-25" />
                <span class="position-absolute top-50 start-50 translate-middle bg-white px-3 text-muted small fw-medium">
                  Don't have an account?
                </span>
              </div>

              <!-- Registration Links -->
              <div class="d-grid gap-2 pt-2">
                <button
                  class="btn btn-outline-success py-2 fw-medium rounded-3"
                  @click="router.push('/student-register')"
                >
                  <i class="bi bi-person-plus me-1"></i> Student Registration
                </button>

                <button
                  class="btn btn-outline-secondary py-2 fw-medium rounded-3"
                  @click="router.push('/company-register')"
                >
                  <i class="bi bi-building-add me-1"></i> Company Registration
                </button>
              </div>

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
import { ref } from "vue";
import { useRouter } from "vue-router";
import api from "../services/api";

const email = ref("");
const password = ref("");
const router = useRouter();

async function login() {
  try {
    const response = await api.post("/login", {
      email: email.value,
      password: password.value,
    });

    alert(response.data.message);

    if (response.data.role === "admin") {
      router.push("/admin");
    } else if (response.data.role === "student") {
      router.push("/student");
    } else if (response.data.role === "company") {
      router.push("/company");
    }
  } catch (error) {
    alert(error.response?.data?.message || "Login failed");
  }
}
</script>

<style scoped>
.login-wrapper {
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