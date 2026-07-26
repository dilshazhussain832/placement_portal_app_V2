<template>
  <div class="container mt-5">

    <h2 class="mb-4">
      Admin Dashboard
    </h2>

    <div class="row">

      <div class="col-md-3 mb-3">
        <div class="card shadow text-center p-3">
          <h5>Students</h5>
          <h2>{{ dashboard.total_students }}</h2>
        </div>
      </div>

      <div class="col-md-3 mb-3">
        <div class="card shadow text-center p-3">
          <h5>Companies</h5>
          <h2>{{ dashboard.total_companies }}</h2>
        </div>
      </div>

      <div class="col-md-3 mb-3">
        <div class="card shadow text-center p-3">
          <h5>Drives</h5>
          <h2>{{ dashboard.total_drives }}</h2>
        </div>
      </div>

      <div class="col-md-3 mb-3">
        <div class="card shadow text-center p-3">
          <h5>Applications</h5>
          <h2>{{ dashboard.total_applications }}</h2>
        </div>
      </div>

    </div>

    <hr class="my-5">

  <h3>Company Management</h3>

  <table class="table table-bordered table-hover mt-3">

    <thead class="table-dark">
      <tr>
        <th>Company</th>
        <th>Industry</th>
        <th>HR Name</th>
        <th>Status</th>
      </tr>
    </thead>

    <tbody>

      <tr v-for="company in companies" :key="company.id">

        <td>{{ company.company_name }}</td>

        <td>{{ company.industry }}</td>

        <td>{{ company.hr_name }}</td>

        <td>
        <span
          class="badge me-2"
          :class="{
            'bg-success': company.approval_status === 'Approved',
            'bg-warning text-dark': company.approval_status === 'Pending',
            'bg-danger': company.approval_status === 'Rejected'
          }"
        >
          {{ company.approval_status }}
        </span>

        <button
          class="btn btn-success btn-sm me-2"
          @click="approveCompany(company.id)"
        >
          Approve
        </button>

        <button
          class="btn btn-danger btn-sm"
          @click="rejectCompany(company.id)"
        >
          Reject
        </button>
      </td>

      </tr>

    </tbody>

  </table>
  <hr class="my-5">

  <h3>Student Management</h3>

  <table class="table table-bordered table-hover mt-3">

    <thead class="table-dark">
      <tr>
        <th>Name</th>
        <th>Branch</th>
        <th>CGPA</th>
        <th>Passing Year</th>
        <th>Skills</th>
      </tr>
    </thead>

    <tbody>

      <tr v-for="student in students" :key="student.id">

        <td>{{ student.full_name }}</td>
        <td>{{ student.branch }}</td>
        <td>{{ student.cgpa }}</td>
        <td>{{ student.passing_year }}</td>
        <td>{{ student.skills }}</td>

      </tr>

    </tbody>

  </table>

  <div class="card shadow mt-4 p-4">

    <h4 class="mb-3">Placement Drives</h4>

    <table class="table table-bordered table-hover">

      <thead>
        <tr>
          <th>Company</th>
          <th>Job Title</th>
          <th>Salary</th>
          <th>Deadline</th>
          <th>Status</th>
          <th>Approval</th>
          <th>Action</th>
        </tr>
      </thead>

      <tbody>

        <tr
          v-for="drive in drives"
          :key="drive.id"
        >

          <td>{{ drive.company_name }}</td>
          <td>{{ drive.job_title }}</td>
          <td>{{ drive.salary }}</td>
          <td>{{ drive.application_deadline }}</td>

          <td>

            <span
              v-if="drive.status === 'Open'"
              class="badge bg-success"
            >
              Open
            </span>

            <span
              v-else
              class="badge bg-danger"
            >
              Closed
            </span>

          </td>

          <td>

            <span
              v-if="drive.approval_status === 'Approved'"
              class="badge bg-success"
            >
              Approved
            </span>

            <span
              v-else-if="drive.approval_status === 'Rejected'"
              class="badge bg-danger"
            >
              Rejected
            </span>

            <span
              v-else
              class="badge bg-warning text-dark"
            >
              Pending
            </span>

          </td>

          <td>

            <button
              class="btn btn-success btn-sm me-2"
              @click="approveDrive(drive.id)"
              :disabled="drive.approval_status === 'Approved'"
            >
              Approve
            </button>

            <button
              class="btn btn-danger btn-sm"
              @click="rejectDrive(drive.id)"
              :disabled="drive.approval_status === 'Rejected'"
            >
              Reject
            </button>

          </td>

        </tr>

      </tbody>

    </table>

  </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import api from "../services/api";

const dashboard = ref({});
const companies = ref([]);
const students = ref([]);
const drives = ref([]);

async function loadDashboard() {
  try {
    const response = await api.get("/admin/dashboard");
    console.log("Dashboard data:", response.data);
    dashboard.value = response.data;
  } catch (error) {
    alert(error.response?.data?.message || "Failed to load dashboard");
  }
}

async function loadCompanies() {
  try {
    const response = await api.get("/admin/companies");
    companies.value = response.data;
  } catch (error) {
    alert(error.response?.data?.message || "Failed to load companies");
  }
}

async function loadStudents() {
  try {
    const response = await api.get("/admin/students");
    students.value = response.data;
  } catch (error) {
    alert(error.response?.data?.message || "Failed to load students");
  }
}

async function approveCompany(id) {
  try {
    await api.put(`/admin/company/${id}/approve`);

    loadCompanies();

    loadDashboard();

  } catch (error) {
    alert(error.response?.data?.message || "Approval failed");
  }
}

async function rejectCompany(id) {
  try {
    await api.put(`/admin/company/${id}/reject`);

    loadCompanies();

    loadDashboard();

  } catch (error) {
    alert(error.response?.data?.message || "Reject failed");
  }
}

const loadDrives = async () => {
  try {
    const response = await api.get("/admin/drives");
    drives.value = response.data;
  } catch (error) {
    console.error(error);
  }
};

const approveDrive = async (id) => {

  try {

    await api.put(`/admin/drive/${id}/approve`);

    alert("Drive approved successfully!");

    await loadDrives();

  } catch (error) {

    alert(
      error.response?.data?.message ||
      "Failed to approve drive."
    );

  }

};

const rejectDrive = async (id) => {

  try {

    await api.put(`/admin/drive/${id}/reject`);

    alert("Drive rejected successfully!");

    await loadDrives();

  } catch (error) {

    alert(
      error.response?.data?.message ||
      "Failed to reject drive."
    );

  }

};

onMounted(() => {
  loadDashboard();
  loadCompanies();
  loadStudents();
  loadDrives();
});
</script>