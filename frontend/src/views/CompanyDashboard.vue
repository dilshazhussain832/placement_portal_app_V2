<template>
  <div class="container mt-5">

    <h2 class="mb-4">
      Company Dashboard
    </h2>

    <div class="card shadow p-4">

      <h4>Create Placement Drive</h4>

      <div class="mb-3">
        <label class="form-label">Job Title</label>
        <input
          class="form-control"
          v-model="job_title"
        >
      </div>

      <div class="mb-3">
        <label class="form-label">Job Description</label>
        <textarea
          class="form-control"
          rows="3"
          v-model="job_description"
        ></textarea>
      </div>

      <div class="mb-3">
        <label class="form-label">Eligibility</label>
        <input
          class="form-control"
          v-model="eligibility"
        >
      </div>

      <div class="mb-3">
        <label class="form-label">Salary</label>
        <input
          class="form-control"
          v-model="salary"
        >
      </div>

      <div class="mb-3">
        <label class="form-label">Application Deadline</label>
        <input
          type="date"
          class="form-control"
          v-model="application_deadline"
        >
      </div>

      <button
        v-if="editingDriveId === null"
        class="btn btn-primary"
        @click="createDrive"
      >
        Create Drive
      </button>

      <button
        v-else
        class="btn btn-success"
        @click="updateDrive"
      >
        Update Drive
      </button>

    </div>

    <div class="card shadow mt-4 p-4">

      <h4 class="mb-3">My Placement Drives</h4>

      <table class="table table-bordered table-hover">

        <thead>
          <tr>
            <th>Job Title</th>
            <th>Eligibility</th>
            <th>Salary</th>
            <th>Deadline</th>
            <th>Status</th>
            <th>Approval</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>

          <tr v-for="drive in drives" :key="drive.id">

            <td>{{ drive.job_title }}</td>
            <td>{{ drive.eligibility }}</td>
            <td>{{ drive.salary }}</td>
            <td>{{ drive.application_deadline }}</td>
            <td>
              <span
                class="badge bg-success"
                v-if="drive.status === 'Open'"
              >
                Open
              </span>

              <span
                class="badge bg-danger"
                v-else
              >
                Closed
              </span>
            </td>
            <td>{{ drive.approval_status }}</td>
            <td>

              <button
                class="btn btn-warning btn-sm me-2"
                @click="editDrive(drive)"
              >
                Edit
              </button>

              <button
                v-if="drive.status === 'Open'"
                class="btn btn-secondary btn-sm me-2"
                @click="toggleStatus(drive.id)"
              >
                Close
              </button>

              <button
                v-else
                class="btn btn-success btn-sm me-2"
                @click="toggleStatus(drive.id)"
              >
                Open
              </button>

              <button
                class="btn btn-danger btn-sm"
                @click="deleteDrive(drive.id)"
              >
                Delete
              </button>

            </td>

          </tr>

        </tbody>

      </table>

    </div>

  </div>
</template>

<script setup>
import api from "../services/api";
import { ref, onMounted } from "vue";

const job_title = ref("");
const job_description = ref("");
const eligibility = ref("");
const salary = ref("");
const application_deadline = ref("");
const drives = ref([]);
const editingDriveId = ref(null);

const createDrive = async () => {
  try {
    await api.post("/company/drive", {
      job_title: job_title.value,
      job_description: job_description.value,
      eligibility: eligibility.value,
      salary: salary.value,
      application_deadline: application_deadline.value,
    });

    alert("Placement drive created successfully!");

    job_title.value = "";
    job_description.value = "";
    eligibility.value = "";
    salary.value = "";
    application_deadline.value = "";

    await loadDrives();

  } catch (error) {
    alert(
      error.response?.data?.message || "Failed to create placement drive."
    );
  }
};

const updateDrive = async () => {
  try {
    await api.put(`/company/drive/${editingDriveId.value}`, {
      job_title: job_title.value,
      job_description: job_description.value,
      eligibility: eligibility.value,
      salary: salary.value,
      application_deadline: application_deadline.value,
    });

    alert("Placement drive updated successfully!");

    editingDriveId.value = null;

    job_title.value = "";
    job_description.value = "";
    eligibility.value = "";
    salary.value = "";
    application_deadline.value = "";

    await loadDrives();

  } catch (error) {
    alert(
      error.response?.data?.message || "Failed to update placement drive."
    );
  }
};

const loadDrives = async () => {
  try {
    const response = await api.get("/company/drives");
    drives.value = response.data;

  } catch (error) {
    console.error(error);
  }
};

onMounted(() => {
  loadDrives();
});

const deleteDrive = async (id) => {
  if (!confirm("Are you sure you want to delete this placement drive?")) {
    return;
  }

  try {
    await api.delete(`/company/drive/${id}`);

    alert("Placement drive deleted successfully!");

    await loadDrives();
  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to delete placement drive."
    );
  }
};

const toggleStatus = async (id) => {
  try {
    const response = await api.put(
      `/company/drive/${id}/toggle-status`
    );

    alert(response.data.message);

    await loadDrives();

  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to update drive status."
    );
  }
};

const editDrive = (drive) => {
  editingDriveId.value = drive.id;

  job_title.value = drive.job_title;
  job_description.value = drive.job_description;
  eligibility.value = drive.eligibility;
  salary.value = drive.salary;
  application_deadline.value = drive.application_deadline;
};

</script>