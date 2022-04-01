# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 11:32:07 2022

@author: bywilson
"""
from connect import *

class create_HN_planning_structures:
    '''Create some of the various HN planning structures including:
        ->shoulder avoid
        ->anterior spare
        
        '''
        
    def __init__(self):
        ##Look for POI's to use
        self.case = get_current("Case")
        self.examination = get_current("Examination")
        
        self.create_shoulder_spare()
        
        
    
    def create_shoulder_spare(self):
        ROI_names = [ROI.Name for ROI in self.case.PatientModel.RegionsOfInterest]
        for POI_name in ['Spare_Shoulder_L','Spare_Shoulder_R']:
            #Look whether there is a point defined
            POIs = self.case.PatientModel.StructureSets[self.examination.Name].PoiGeometries
            for p in POIs:
                if p.OfPoi.Name == POI_name:
                    ##look whether point is defined
                    if p.Point != None:
                        ###create shoulder spare from the point
                        self.create_cylinder_structure(p.Point,POI_name)
                        
                        if POI_name in ROI_names:
                            ROI_name = POI_name
                            self.case.PatientModel.RegionsOfInterest[ROI_name].UpdateDerivedGeometry(Examination= self.examination)
                        else:
                            print('could not find shoulder spare structure create and update manually')
                                            
                    else:
                        print('Could not find geometry')
            else:
                print('Could not find point')
           
        
    def create_cylinder_structure(self,point_centre, POI_name):
        
        ##look for cylinder avoid structure
        if "L" == POI_namep[-1]:
            ROI_name = 'NS_cylshoulder_L'
        else:
            ROI_name = 'NS_cylshoulder_R'
        
        ##Look whether the ROI exists, if not create it
        for ROI in reversed(self.case.PatientModel.RegionsOfInterest):
            print(ROI.Name)
            if ROI.Name == ROI_name:
                ROI_to_use = ROI
                break
        else:
            ##create the ROI
            ROI_to_use = self.case.PatientModel.CreateRoi(
                Name=ROI_name, Color="Orange", Type="Undefined", 
                TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
        
        
        ##Create ROI from spherical expansion of POI
        ROI_to_use.CreateCylinderGeometry(
            Radius=10, Axis={ 'x': 0, 'y': 0, 'z': 1 }, Length=5,
            Examination=self.examination, Center = point_centre,
            Representation="TriangleMesh", VoxelSize=None)


def do_task(*Options):
    create_HN_planning_structures()
    
  

if __name__ == '__main__':
    create_HN_planning_structures()
    
    
