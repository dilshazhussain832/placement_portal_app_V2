<template>
  <div class="container mt-5">

    <h2 class="mb-4">
      Student Dashboard
    </h2>

    <div class="card shadow p-4">

      <h4 class="mb-3">
        Available Placement Drives
      </h4>

      <table class="table table-bordered table-hover">

        <thead>

          <tr>
            <th>Company</th>
            <th>Job Title</th>
            <th>Eligibility</th>
            <th>Salary</th>
            <th>Deadline</th>
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
            <td>{{ drive.eligibility }}</td>
            <td>{{ drive.salary }}</td>
            <td>{{ drive.application_deadline }}</td>

            <td>

              <button
                v-if="!hasApplied(drive.id)"
                class="btn btn-primary btn-sm"
                @click="applyForDrive(drive.id)"
              >
                Apply
              </button>

              <button
                v-else
                class="btn btn-success btn-sm"
                disabled
              >
                Applied
              </button>

            </td>

          </tr>

        </tbody>

      </table>

    </div>

    <div class="card shadow mt-4 p-4">

      <h4 class="mb-3">
        My Applications
      </h4>

      <table class="table table-bordered table-hover">

        <thead>
          <tr>
            <th>Company</th>
            <th>Job Title</th>
            <th>Applied On</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>

          <tr
            v-for="application in applications"
            :key="application.application_id"
          >

            <td>{{ application.company_name }}</td>
            <td>{{ application.job_title }}</td>
            <td>{{ application.application_date }}</td>

            <td>

              <span
                v-if="application.status === 'Applied'"
                class="badge bg-primary"
              >
                Applied
              </span>

              <span
                v-else-if="application.status === 'Shortlisted'"
                class="badge bg-success"
              >
                Shortlisted
              </span>

              <span
                v-else-if="application.status === 'Rejected'"
                class="badge bg-danger"
              >
                Rejected
              </span>

              <span
                v-else
                class="badge bg-secondary"
              >
                {{ application.status }}
              </span>

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

const drives = ref([]);
const applications = ref([]);

const loadDrives = async () => {
  try {
    const response = await api.get("/student/drives");
    drives.value = response.data;
  } catch (error) {
    console.error(error);
  }
};

const loadApplications = async () => {
  try {
    const response = await api.get("/student/applications");
    applications.value = response.data;
  } catch (error) {
    console.error(error);
  }
};

const applyForDrive = async (driveId) => {
  try {
    const response = await api.post(`/student/apply/${driveId}`);

    alert(response.data.message);

    await loadDrives();
    await loadApplications();

  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to apply."
    );
  }
};

const hasApplied = (driveId) => {
  return applications.value.some(
    application => application.drive_id === driveId
  );
};

onMounted(() => {
  loadDrives();
  loadApplications();
});
</script>