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
            <th>Applicants</th>
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

              <template v-if="drive.approval_status !== 'Approved'">

                <button
                  class="btn btn-warning btn-sm me-2"
                  @click="editDrive(drive)"
                >
                  Edit
                </button>

                <button
                  class="btn btn-danger btn-sm me-2"
                  @click="deleteDrive(drive.id)"
                >
                  Delete
                </button>

              </template>

              <span
                v-else
                class="badge bg-success"
              >
                Approved - Locked
              </span>

              

            </td>
            <td>

              <button
                v-if="drive.approval_status === 'Approved'"
                class="btn btn-info btn-sm"
                @click="loadApplicants(drive)"
              >
                View Applicants
              </button>

              <span
                v-else
                class="badge bg-secondary"
              >
                Not Available
              </span>

            </td>

          </tr>

        </tbody>

      </table>

    </div>
    <div
      v-if="selectedDrive"
      class="card shadow mt-4 p-4"
    >

      <h4 class="mb-3">
        Applicants for {{ selectedDrive.job_title }}
      </h4>

      <table class="table table-bordered table-hover">

        <thead>

          <tr>

            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Branch</th>
            <th>CGPA</th>
            <th>Skills</th>
            <th>Status</th>
            <th>Action</th>

          </tr>

        </thead>

        <tbody>

          <tr
            v-for="applicant in applicants"
            :key="applicant.application_id"
          >

            <td>{{ applicant.student_name }}</td>
            <td>{{ applicant.email }}</td>
            <td>{{ applicant.phone }}</td>
            <td>{{ applicant.branch }}</td>
            <td>{{ applicant.cgpa }}</td>
            <td>{{ applicant.skills }}</td>

            <td>

              <span
                v-if="applicant.status === 'Applied'"
                class="badge bg-primary"
              >
                Applied
              </span>

              <span
                v-else-if="applicant.status === 'Shortlisted'"
                class="badge bg-success"
              >
                Shortlisted
              </span>

              <span
                v-else-if="applicant.status === 'Rejected'"
                class="badge bg-danger"
              >
                Rejected
              </span>

              <span
                v-else
                class="badge bg-secondary"
              >
                {{ applicant.status }}
              </span>

            </td>

            <td>

              <template v-if="applicant.status === 'Applied'">

                <button
                  class="btn btn-success btn-sm me-2"
                  @click="shortlistApplicant(applicant.application_id)"
                >
                  Shortlist
                </button>

                <button
                  class="btn btn-danger btn-sm"
                  @click="rejectApplicant(applicant.application_id)"
                >
                  Reject
                </button>

              </template>

              <span
                v-else-if="applicant.status === 'Shortlisted'"
                class="badge bg-success"
              >
                Final Decision
              </span>

              <span
                v-else
                class="badge bg-danger"
              >
                Final Decision
              </span>

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
const applicants = ref([]);
const selectedDrive = ref(null);

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

const loadApplicants = async (drive) => {

  try {

    const response = await api.get(
      `/company/drive/${drive.id}/applications`
    );

    applicants.value = response.data;
    selectedDrive.value = drive;

  } catch (error) {

    alert(
      error.response?.data?.message ||
      "Failed to load applicants."
    );

  }

};
const shortlistApplicant = async (applicationId) => {
  try {
    const response = await api.put(
      `/company/application/${applicationId}/shortlist`
    );

    alert(response.data.message);

    await loadApplicants(selectedDrive.value);

  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to shortlist applicant."
    );
  }
};

const rejectApplicant = async (applicationId) => {
  try {
    const response = await api.put(
      `/company/application/${applicationId}/reject`
    );

    alert(response.data.message);

    await loadApplicants(selectedDrive.value);

  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to reject applicant."
    );
  }
};

</script>