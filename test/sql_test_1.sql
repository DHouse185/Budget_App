SELECT states_income_tax_test.single_filer_rates, states_income_tax_test.single_filer_brackets,
states_income_tax_test.standard_deduction_single 
FROM states_income_tax_test
INNER JOIN states_test
ON states_income_tax_test.state_id = states_test.state_id
WHERE states_test.state_name = 'Kansas';