# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:46:05 2022

@author: bywilson
"""

from connect import *

class initial_optimization():
    def __init__(self):
        self.plan = get_current("Plan")
        self.examination = get_current('Examination')
        self.case = get_current('Case')
        
        self.delete_broken_functions()
        self.optimize()
        
        # plan.PlanOptimizations[0].Objective.ConstituentFunctions[0].ForRegionOfInterest.Name
        # #delete cost functions with undefined structures
        # plan.PlanOptimizations[0].Objective.ConstituentFunctions[-1].DeleteFunction()


    def delete_broken_functions(self):

        has_contours = {} #create dictionary because it takes a while to check for contours per structure
        for f in self.plan.PlanOptimizations[0].Objective.ConstituentFunctions:
            print('HELLO3')
            ROI_name = f.ForRegionOfInterest.Name
            if ROI_name in has_contours:
                if has_contours[ROI_name] == False:
                    f.DeleteFunction()
                    print('HELLO2')
                    
            else: #figure out whether it has contours, if not delete
                ROI_geo = self.case.PatientModel.StructureSets[self.examination.Name].RoiGeometries[ROI_name]
                has_contours[ROI_name] = ROI_geo.HasContours()
                if has_contours[ROI_name] == False:
                    print('HELLO')
                    f.DeleteFunction()

        
        
    def optimize(self):
        for i in range(3):
            self.plan.PlanOptimizations[0].RunOptimization()

if __name__ == '__main__':
    initial_optimization()