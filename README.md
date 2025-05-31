# ASE 2025 Experience Report
Data and Replication Package for ASE 2025 Experience Report.

**How to run:**

1. Install the required libraries.
2. Configure the openai API if you want LLM suggested fix.
3. Switch to the root folder.
4. Run `pytest test/test_aa.py --autofix-mode=suggest` to run the test cases for aa.com with LLM fix if failed (similar to other tests).
5. Check the log file in the testoutput folder.