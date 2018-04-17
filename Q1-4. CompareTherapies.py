import ParameterClasses as P
import MarkovModelClasses as MarkovCls
import SupportMarkovModel as SupportMarkov


# NO ANTICOAGULANT
# create a cohort
cohort_none = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE)
# simulate the cohort
simOutputs_none = cohort_none.simulate()

# ANTICOAGULANT
# create a cohort
cohort_anticoag = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.ANTICOAG)
# simulate the cohort
simOutputs_anticoag = cohort_anticoag.simulate()

# draw survival curves and histograms
SupportMarkov.draw_survival_curves_and_histograms(simOutputs_none, simOutputs_anticoag)

print('Problem 1')
# print the estimates
SupportMarkov.print_outcomes(simOutputs_none, "No Anticoagulant:")
SupportMarkov.print_outcomes(simOutputs_anticoag, "Anticoagulant:")
print('   ')

# print comparative outcomes
print('Problem 2')
SupportMarkov.print_comparative_outcomes(simOutputs_none, simOutputs_anticoag)
print('  ')

# report the CEA results
print('Problems 3: please see CEATable and the CEA figure.')
SupportMarkov.report_CEA_CBA(simOutputs_none, simOutputs_anticoag)
print('   ')

print('Problem 4')
print('Based on the CBA figure, I would recommend anticoagulant if the willingness to pay level is above $9000.')
