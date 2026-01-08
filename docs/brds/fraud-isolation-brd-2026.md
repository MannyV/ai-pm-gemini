# BRD: Granular Fraud Isolation for Vendor-Locked Cards

**Document Status:** Draft  
**Last Updated:** January 8, 2026  
**Author:** Planning Agent (Gemini 2.5 Pro)  
**Target Release:** Q2 2026

---

## 1. Executive Summary
Currently, corporate card users (specifically Ramp users) experience significant operational downtime when a single fraudulent transaction occurs on a merchant-locked card. Because the current security protocol requires a full card cancellation, all legitimate recurring payments to that vendor are severed. 

This document specifies the **"Granular Fraud Isolation" (GFI)** feature, which allows users to dispute specific transactions while keeping the underlying merchant-token relationship intact through dynamic token rotation and predictive fraud shielding.

---

## 2. Problem Statement
*   **The Problem:** High-volume SaaS subscriptions (e.g., AWS, Slack) often use "merchant-locked" cards. If one fraudulent charge appears, the manager must kill the card.
*   **The Impact:** Breaking the card breaks the integration. Re-authenticating a corporate card across 50+ Slack workspaces or complex AWS accounts can take hours of manual labor and cause service interruptions.
*   **The Need:** A way to "quarantine" a charge and rotate the security credentials without notifying the merchant or breaking the billing relationship.

---

## 3. Technical Requirements

### 3.1 Merchant-Token Rotation (MTR)
*   **Requirement:** The system must generate a "Shadow Token" for the merchant whenever a dispute is initiated.
*   **Mechanism:** Leverage Visa/Mastercard Digital Enablement Service (MDES/VTS) to rotate the underlying token without invalidating the Merchant-on-File (CoF) agreement.
*   **User Flow:** User clicks "Dispute & Isolate" -> System requests new token from network -> System updates internal routing -> Previous token is blacklisted for that specific transaction ID but remains "monitoring" for others if necessary.

### 3.2 Predictive Fraud Shield
*   **Requirement:** After a dispute, the system must apply a 48-hour "Strict Mode" for that specific merchant.
*   **Logic:** Any transaction from that merchant that deviates >5% from the historical average must be auto-quarantined and sent for SMS/App approval.

---

## 4. User Stories

### US-001: The "Keep the Lights On" Dispute
**As a** Finance Manager  
**I want to** dispute a $19.99 unknown charge on my $50k/month AWS card  
**So that** I don't have to re-enter card details in 15 different AWS regions and break our infrastructure.

**Acceptance Criteria:**
- [ ] User selects a single transaction from the feed.
- [ ] User selects "Dispute & Isolate Card."
- [ ] System confirms: "Legitimate transactions with [Merchant] will continue. We are rotating your security token."
- [ ] Underlying card number (PAN) remains unchanged for the merchant interface.

---

## 5. Task Breakdown Structure

### Phase 1: Network Integration (Backend)
- **TASK-001:** Implement VTS/MDES Token Refresh API call.
- **TASK-002:** Create "Shadow Token" mapping layer in the transaction router.
- **TASK-003:** Build transaction blacklisting logic for specific IDs.

### Phase 2: UI/UX (Frontend)
- **TASK-004:** Add "Dispute & Isolate" button to transaction detail view.
- **TASK-005:** Build the "Isolation Status" dashboard for cards in "Strict Mode."

---

## 6. Success Metrics
*   **Reduction in Card Re-issuances:** Target 40% reduction for merchant-locked cards.
*   **Time-to-Recovery:** Reduce the time a merchant spends in "Billing Error" state from 2 hours (avg) to 0 minutes.
*   **User Sentiment:** Measured via NPS following a successful isolation event.

---

## 7. Risks & Mitigations
*   **Risk:** The network rejects the token rotation request.
*   **Mitigation:** Fallback to standard "Freeze Card" with a prompt to the user to contact the merchant manually.
*   **Risk:** The merchant detects the token change as a fraud risk themselves.
*   **Mitigation:** Use "Reason Code: Security Refresh" during network update to signal a non-billing-failure event.
