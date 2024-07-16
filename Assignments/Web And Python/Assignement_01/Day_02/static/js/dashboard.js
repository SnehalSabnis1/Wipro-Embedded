
function showPolicyDetails(policyId) {
    // In a real application, you would fetch these details from the server
    var policyDetails = {
        12345: {
            policyId: "12345",
            policyHolder: "John Doe",
            policyStatus: "Active"
        }
        // Add more policy details as needed
    };

    var details = policyDetails[policyId];
    if (details) {
        document.getElementById('policyId').textContent = "Policy ID: " + details.policyId;
        document.getElementById('policyHolder').textContent = "Policyholder: " + details.policyHolder;
        document.getElementById('policyStatus').textContent = "Status: " + details.policyStatus;
    }
}

function sortPolicies(criteria) {
    var policyList = document.getElementById('policy-list');
    var policies = Array.from(policyList.getElementsByClassName('policy-card'));

    policies.sort(function(a, b) {
        var aValue = a.getAttribute('data-' + criteria);
        var bValue = b.getAttribute('data-' + criteria);
        if (aValue < bValue) return -1;
        if (aValue > bValue) return 1;
        return 0;
    });

    policies.forEach(function(policy) {
        policyList.appendChild(policy);
    });
}

