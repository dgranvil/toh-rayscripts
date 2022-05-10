# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 11:24:11 2021
##Tested on cpython 3.6
@author: bywilson

Bug: add in check to see whether course exists and create unique name if it does
"""
from connect import *


class apply_clinical_goals :
    def __init__(self, care_plan):
        ##init things

        self.db = get_current("PatientDB")
        self.plan = get_current('Plan')
        self.careplan = care_plan
        

    def apply_clinical_goals(self):
        
        template_list = [x['Name'] for x in self.db.GetClinicalGoalTemplateInfo() if self.careplan in x['Name']]

        if len(template_list) == 1:
            template_name = template_list[0]
            clinical_goals_template = self.db.LoadTemplateClinicalGoals(templateName = template_name, lockMode = 'Read')
            self.plan.TreatmentCourse.EvaluationSetup.ApplyClinicalGoalTemplate(Template=clinical_goals_template)
            clinical_goals_template.Unload()
        elif len(template_list) > 1:
            popup_cg = popup('Select clinical goal template below', 
                options=template_list, 
                text_input_label="Select template" 
                ) 
            template_name = popup_cg['option']
            clinical_goals_template = self.db.LoadTemplateClinicalGoals(templateName = template_name, lockMode = 'Read')
            self.plan.TreatmentCourse.EvaluationSetup.ApplyClinicalGoalTemplate(Template=clinical_goals_template)
            clinical_goals_template.Unload()
        else:
            show_result_message('No matching clinical goal templates were found. Clinical goals not loaded.', level='warn') 

def do_task(**options):
    
    print(options)
    apply_clinical_goals(care_plan = options[ 'selected_careplan']).apply_clinical_goals()
   
    return
        
