from connect import *


class load_structure_template:
    
    def __init__(self):
        self.case = get_current("Case")
        self.examination = get_current("Examination")
        self.db = get_current("PatientDB")
        
        # Dict with keys = name of structure template in RayStation
        #           values = list of applicable careplans as defined in rayscripts confid
        self.template_matching_OARs = {'H&N IMRT 7000 6300 5600 SS' : ['H&N IMRT 7000 6300 5600']
        }
        self.bone_structure = 'NS_bone'
        
        

    def load_template(self, selected_careplan): 
        # Decide which template to use  
        for template in self.template_matching_OARs.keys():
            if selected_careplan in self.template_matching_OARs[template]:
                T = self.db.LoadTemplatePatientModel(templateName = template)
                source_ROI_names = T.PatientModel.RegionsOfInterest.Keys
                source_POI_names = T.PatientModel.PointsOfInterest.Keys
                self.case.PatientModel.CreateStructuresFromTemplate(
                    SourceTemplate = T,
                    SourceExaminationName=T.StructureSetExaminations[0].Name,
                    SourceRoiNames=source_ROI_names, 
                    SourcePoiNames=source_POI_names,
                    AssociateStructuresByName=True, TargetExamination=self.examination, InitializationOption="EmptyGeometries")
                T.Unload()

                break
            
        self.create_bone_contour()
        self.create_air_contour()
            

        
        
    def create_bone_contour(self):
        #If the template has bone structure in it, try to create the auto bone structure
        #Find external contour        
        bone_structure = 'NS_bone'
        if self.contour_exists_and_empty(bone_structure):
            for ROI in  self.case.PatientModel.RegionsOfInterest :
                if ROI.Type == 'External':
                    external = ROI
                    break
            else:
                return

            with CompositeAction('Create bone ROI ('+bone_structure + ')'):
    
                self.case.PatientModel.RegionsOfInterest[bone_structure].BoneSegmentationByRegionGrowing(
                    ExaminationName=self.examination.Name, DelimitingRoiGeometryName=external.Name,
                    BoneSeedThreshold=200, TissueSeedThreshold=100)

            



    def create_air_contour(self):
        air_ROI = 'NS_LowDensity'
        if self.contour_exists_and_empty(air_ROI):
            with CompositeAction('Create Air ROI ('+air_ROI + ')'):
                self.case.PatientModel.RegionsOfInterest[air_ROI].GrayLevelThreshold(Examination=self.examination, LowThreshold=-1024, HighThreshold=-206, PetUnit=r"", CbctUnit=None, BoundingBox=None)
        
                self.case.PatientModel.StructureSets[self.examination.Name].SimplifyContours(
                    RoiNames=[air_ROI], RemoveHoles3D=False, RemoveSmallContours=True, AreaThreshold=0.2, ReduceMaxNumberOfPointsInContours=False, MaxNumberOfPoints=None, CreateCopyOfRoi=False, ResolveOverlappingContours=True)
            
    def contour_exists_and_empty(self, contour_name):
        ROI_names = self.case.PatientModel.RegionsOfInterest.Keys
        if contour_name in ROI_names:
            contour_geometry = self.case.PatientModel.StructureSets[self.examination.Name].RoiGeometries[contour_name]
            if not contour_geometry.HasContours():
                return 1
            else:
                return 0
            
        return 0

def do_task(**options):
    load_structure_template().load_template(selected_careplan = options['selected_careplan'])

if __name__ == '__main__':
     load_structure_template().load_template(selected_careplan ='H&N IMRT')