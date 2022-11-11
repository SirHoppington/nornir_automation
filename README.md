# ci-cd-net

A repo to be used as a "Golden branch" for network device configuration as part of
a Network DevOps CI/CD pipeline.

Nornir CI/CD Pipeline workflow:

1. Engineer clones main repo.

2. Engineer modifies configuration in "/crq_changes" and pushes to feature branch.

3. Webhook triggers Jenkins Pipeline.
   1. Configuration pushed to Dev environment for only configs changed (diff on /crq_changes and /gold_config):
      1. Dry-run of configuration changes run
      2. Napalm/nornir send configuration changes to devices concurrently
      3. Gold config is updated in feature branch to reflect config changes

### To be added:
4. PyATS post test scripts run 
   1. pull request made to main branch
5. Peer review/CAB of proposed changes.
6. Merge to main branch.
7. Webhook triggers Jenkins Pipeline for Prod.
   1. steps 3.i and 3.ii rerun