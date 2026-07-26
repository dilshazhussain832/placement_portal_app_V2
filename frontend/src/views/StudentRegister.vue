<template>
  <div class="container py-5 d-flex justify-content-center">
    <div class="card shadow p-4" style="max-width: 550px; width: 100%;">

      <h2 class="text-center mb-2">Student Registration</h2>
      <p class="text-center text-muted mb-4">
        Create your student account
      </p>

      <form @submit.prevent="registerStudent">

        <div class="mb-3">
          <label class="form-label">Full Name</label>
          <input
            v-model="form.full_name"
            type="text"
            class="form-control"
            required
          >
        </div>

        <div class="mb-3">
          <label class="form-label">Email</label>
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

        <div class="mb-3">
          <label class="form-label">Phone</label>
          <input
            v-model="form.phone"
            type="text"
            class="form-control"
            required
          >
        </div>

        <div class="mb-3">
          <label class="form-label">Branch</label>
          <input
            v-model="form.branch"
            type="text"
            class="form-control"
            placeholder="e.g. CSE, Data Science"
            required
          >
        </div>

        <div class="mb-3">
          <label class="form-label">CGPA</label>
          <input
            v-model="form.cgpa"
            type="number"
            step="0.01"
            class="form-control"
            required
          >
        </div>

        <div class="mb-3">
          <label class="form-label">Passing Year</label>
          <input
            v-model="form.passing_year"
            type="number"
            class="form-control"
            required
          >
        </div>

        <div class="mb-3">
          <label class="form-label">Skills</label>
          <textarea
            v-model="form.skills"
            class="form-control"
            rows="3"
            placeholder="Python, SQL, Java"
            required
          ></textarea>
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

    router.push("/");

  } catch (error) {

    alert(
      error.response?.data?.message ||
      "Registration failed"
    );

  }
}
</script>