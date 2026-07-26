<template>
  <div class="container py-5 d-flex justify-content-center">
    <div class="card shadow p-4" style="max-width: 550px; width: 100%;">

      <h2 class="text-center mb-2">Company Registration</h2>
      <p class="text-center text-muted mb-4">
        Register your company
      </p>

      <form @submit.prevent="registerCompany">

        <div class="mb-3">
          <label class="form-label">Company Name</label>
          <input
            v-model="form.company_name"
            type="text"
            class="form-control"
            required
          >
        </div>

        <div class="mb-3">
          <label class="form-label">Industry</label>
          <input
            v-model="form.industry"
            type="text"
            class="form-control"
            required
          >
        </div>

        <div class="mb-3">
          <label class="form-label">Website</label>
          <input
            v-model="form.website"
            type="text"
            class="form-control"
            placeholder="https://example.com"
          >
        </div>

        <div class="mb-3">
          <label class="form-label">HR Name</label>
          <input
            v-model="form.hr_name"
            type="text"
            class="form-control"
            required
          >
        </div>

        <div class="mb-3">
          <label class="form-label">HR Email</label>
          <input
            v-model="form.hr_email"
            type="email"
            class="form-control"
            required
          >
        </div>

        <div class="mb-3">
          <label class="form-label">Login Email</label>
          <input
            v-model="form.email"
            type="email"
            class="form-control"
            required
          >
        </div>

        <div class="mb-3">
          <label class="form-label">Password</label>
          <input
            v-model="form.password"
            type="password"
            class="form-control"
            required
          >
        </div>

        <button
          type="submit"
          class="btn btn-primary w-100 mb-2"
        >
          Register
        </button>

        <button
          type="button"
          class="btn btn-secondary w-100"
          @click="router.push('/')"
        >
          Back to Login
        </button>

      </form>

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

    router.push("/");

  } catch (error) {

    alert(
      error.response?.data?.message ||
      "Registration failed"
    );

  }
}
</script>