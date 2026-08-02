<template>
  <div class="register-wrapper min-vh-100 d-flex justify-content-center align-items-center py-5">
    <div class="container py-3">
      <div class="row justify-content-center">
        <div class="col-12 col-md-10 col-lg-7 col-xl-6">

          <div class="card border-0 shadow-lg rounded-4 overflow-hidden">
            <!-- Header Accent Bar -->
            <div class="bg-emerald py-1"></div>

            <div class="card-body p-4 p-sm-5">

              <!-- Header -->
              <div class="text-center mb-4">
                <div class="brand-badge bg-success-subtle text-success mb-3 mx-auto">
                  <i class="bi bi-building-add fs-3"></i>
                </div>
                <h2 class="fw-bold text-dark h3 mb-1">Company Registration</h2>
                <p class="text-secondary small mb-0">
                  Register your company to post placement drives and hire talent
                </p>
              </div>

              <form @submit.prevent="registerCompany">

                <!-- Company Name & Industry -->
                <div class="row g-3 mb-3">
                  <div class="col-12 col-md-6">
                    <label class="form-label fw-semibold text-secondary small">Company Name</label>
                    <div class="input-group">
                      <span class="input-group-text bg-light border-end-0 text-muted">
                        <i class="bi bi-building"></i>
                      </span>
                      <input
                        v-model="form.company_name"
                        type="text"
                        class="form-control bg-light border-start-0 ps-0"
                        placeholder="Acme Corp"
                        required
                      >
                    </div>
                  </div>

                  <div class="col-12 col-md-6">
                    <label class="form-label fw-semibold text-secondary small">Industry</label>
                    <div class="input-group">
                      <span class="input-group-text bg-light border-end-0 text-muted">
                        <i class="bi bi-briefcase"></i>
                      </span>
                      <input
                        v-model="form.industry"
                        type="text"
                        class="form-control bg-light border-start-0 ps-0"
                        placeholder="IT & Software"
                        required
                      >
                    </div>
                  </div>
                </div>

                <!-- Website & HR Name -->
                <div class="row g-3 mb-3">
                  <div class="col-12 col-md-6">
                    <label class="form-label fw-semibold text-secondary small">Company Website</label>
                    <div class="input-group">
                      <span class="input-group-text bg-light border-end-0 text-muted">
                        <i class="bi bi-globe"></i>
                      </span>
                      <input
                        v-model="form.website"
                        type="text"
                        class="form-control bg-light border-start-0 ps-0"
                        placeholder="https://example.com"
                      >
                    </div>
                  </div>

                  <div class="col-12 col-md-6">
                    <label class="form-label fw-semibold text-secondary small">HR Name</label>
                    <div class="input-group">
                      <span class="input-group-text bg-light border-end-0 text-muted">
                        <i class="bi bi-person-badge"></i>
                      </span>
                      <input
                        v-model="form.hr_name"
                        type="text"
                        class="form-control bg-light border-start-0 ps-0"
                        placeholder="Jane Smith"
                        required
                      >
                    </div>
                  </div>
                </div>

                <!-- HR Email & Login Email -->
                <div class="row g-3 mb-3">
                  <div class="col-12 col-md-6">
                    <label class="form-label fw-semibold text-secondary small">HR Contact Email</label>
                    <div class="input-group">
                      <span class="input-group-text bg-light border-end-0 text-muted">
                        <i class="bi bi-envelope-at"></i>
                      </span>
                      <input
                        v-model="form.hr_email"
                        type="email"
                        class="form-control bg-light border-start-0 ps-0"
                        placeholder="hr@example.com"
                        required
                      >
                    </div>
                  </div>

                  <div class="col-12 col-md-6">
                    <label class="form-label fw-semibold text-secondary small">Login Email</label>
                    <div class="input-group">
                      <span class="input-group-text bg-light border-end-0 text-muted">
                        <i class="bi bi-envelope"></i>
                      </span>
                      <input
                        v-model="form.email"
                        type="email"
                        class="form-control bg-light border-start-0 ps-0"
                        placeholder="login@example.com"
                        required
                      >
                    </div>
                  </div>
                </div>

                <!-- Password -->
                <div class="mb-4">
                  <label class="form-label fw-semibold text-secondary small">Account Password</label>
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

                <!-- Action Buttons -->
                <button
                  type="submit"
                  class="btn btn-emerald w-100 py-2-5 mb-2 fw-semibold rounded-3 shadow-sm"
                >
                  <i class="bi bi-check-circle me-1"></i> Register Company
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
  company_name: "",
  industry: "",
  website: "",
  hr_name: "",
  hr_email: "",
  email: "",
  password: ""
});

async function registerCompany() {
  try {
    const response = await api.post(
      "/company/register",
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
  background: radial-gradient(circle at 50% 10%, rgba(16, 185, 129, 0.08) 0%, rgba(248, 250, 252, 1) 70%);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

.bg-emerald {
  background-color: #10b981;
}

.btn-emerald {
  background-color: #10b981;
  color: #ffffff;
  border: none;
}

.btn-emerald:hover {
  background-color: #059669;
  color: #ffffff;
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
  border-color: #10b981;
}

.input-group:focus-within .input-group-text {
  background-color: #ffffff !important;
  border-color: #10b981;
  color: #10b981 !important;
}

.py-2-5 {
  padding-top: 0.65rem;
  padding-bottom: 0.65rem;
}
</style>