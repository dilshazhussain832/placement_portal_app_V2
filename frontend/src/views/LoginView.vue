<template>
  <div class="container vh-100 d-flex justify-content-center align-items-center">
    <div class="card shadow p-4" style="width: 400px">

      <h2 class="text-center mb-2">Placement Portal</h2>
      <p class="text-center text-muted mb-4">
        IIT Madras Placement Portal
      </p>

      <div class="mb-3">
        <label class="form-label">Email</label>
        <input
          type="email"
          class="form-control"
          v-model="email"
          placeholder="Enter email"
        >
      </div>

      <div class="mb-3">
        <label class="form-label">Password</label>
        <input
          type="password"
          class="form-control"
          v-model="password"
          placeholder="Enter password"
        >
      </div>

      <button
        class="btn btn-primary w-100 mb-3"
        @click="login"
      >
        Login
      </button>

      <div class="d-grid gap-2">
        <button
          class="btn btn-outline-success"
          @click="router.push('/student-register')"
        >
          Student Registration
        </button>

        <button
          class="btn btn-outline-secondary"
          @click="router.push('/company-register')"
        >
          Company Registration
        </button>
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