import pandas as pd

################################################################
##              Information and dictionary
################################################################

'''Resident_Status = line[19].strip()'''
Resident = {1: 'RESIDENTS - State and County of Occurrence and Residence are the same.',
2: 'INTRASTATE NONRESIDENTS - State of Occurrence and Residence are the same, but County is different.',
3: 'INTERSTATE NONRESIDENTS - State of Occurrence and Residence are different, but both are in the U.S.',
4: 'FOREIGN RESIDENTS - State of Occurrence is one of the 50 States or the District of Columbia, but Place of Residence is outside of the U.S.'}

'''Education = line[60:62].strip()'''

education = {0: 'No formal education',
 4:  '4 Years of elementary school',
 6:  '6 Years of elementary school',
 7:  '7 Years of elementary school',
 8: '8 Years of elementary school',
 9: '1 year of high school',
 10: '2 years of high school',
 11: '3 years of high school',
 12: '4 years of high school',
 13: '1 year of college',
 14: '2 years of college',
 15: '3 years of college',
 16: '4 years of college',
 17: '5 or more years of college',
 99: 'not stated'
}

'''Month_Of_Death = line[63:67].strip()'''
'''values: [1,2,3,4, 5,6,7,8,9,10,11,12]'''
month_of_death = {1: 'Jan', 2: 'Feb', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'Sep' , 10: 'Oct', 11: 'Nov', 12: 'Dec'}


'''Sex = line[68].strip()'''
sex = {1: 'female', 0:'male'}

'''Age_Key = line[69].strip()'''
'''not sure '''

'''Age_Value = line[70:73].strip()'''
'''Value is age in years, one is 999'''

'''Age_Sub_Flag = line[73].strip()'''
'''not taken into account
Blank  Calculated age is not substituted for reported age
1  Calculated age is substituted for reported age
'''

'''Age_Recode_52 = line[74:76].strip()
Age_Recode_27 = line[76:78].strip()
Age_Recode_12 = line[78:80].strip()'''
'''binning ages to for age groups, we keep Age_Recode_12'''

Age_Recode_12 = {1: 'Under 1 year (includes not stated infant ages)',
2: '1 - 4 years',
3: '5 - 14 years',
4: '15 - 24 years',
5: '25 - 34 years',
6: '35 - 44 years',
7: '45 - 54 years',
8: '55 - 64 years',
9: '65 - 74 years',
10: '75 - 84 years',
11: '85 years and over',
12: 'Age not stated'}

'''Infant_Age_Recode_22 = line[80:82].strip()'''
'''value not used'''

'''Place_Of_Death = line[82].strip()'''

place_of_death = {1: 'Hospital, clinic or Medical Center - Inpatient',
2: 'Hospital, Clinic or Medical Center - Outpatient or admitted to Emergency Room',
3: 'Hospital, Clinic or Medical Center - Dead on Arrival',
4: 'Decedent s home',
5: 'Hospice facility',
6: 'Nursing home/long term care',
7: 'Other',
9: 'Place of death unknown'}

'''Marital_Status = line[83].strip()'''
marital_status = {'1': 'S - never married, single',
'2': 'M - Marries',
'3': 'D - Divorced',
'4': 'W - Widowed',
'5': 'U - Marital Status unknown'}

'''DOW_of_Death = line[84].strip()'''
'''Day of the week of death'''
DOW = {1: 'Sunday',
2: 'Monday',
3: 'Tuesday',
4: 'Wednesday',
5: 'Thursday',
6: 'Friday',
7: 'Saturday',
9: 'Unknown'}

'''Data_Year = line[101:105].strip()'''
'''not used'''
'''Injured_At_Work = line[105].strip()'''
'''not used'''

'''Manner_Of_Death = line[106].strip()'''
'''Value 2 denotes suicide'''

'''Method_Of_Disposition = line[107].strip()
Autopsy = line[108].strip()
Activity_Code = line[143].strip()
Place_Of_Causal_Injury = line[144].strip()
ICD10 = line[145:149].strip()
Cause_Recode_358 = line[149:152].strip()
Cause_Recode_113 = line[153:156].strip()
Infant_Cause_Recode_130 = line[156:159].strip()
Cause_Recode_39 = line[159:161].strip()
Entity_Axis_Conditions = line[162:164].strip()
EAC1 = line[164:171].strip()
EAC2 = line[171:178].strip()
EAC3 = line[178:185].strip()
EAC4 = line[185:192].strip()
EAC5 = line[192:199].strip()
EAC6 = line[199:206].strip()
EAC7 = line[206:213].strip()
EAC8 = line[213:220].strip()
EAC9 = line[220:227].strip()
EAC10 = line[227:234].strip()
EAC11 = line[234:241].strip()
EAC12 = line[241:248].strip()
EAC13 = line[248:255].strip()
EAC14 = line[255:262].strip()
EAC15 = line[262:269].strip()
EAC16 = line[269:276].strip()
EAC17 = line[276:283].strip()
EAC18 = line[283:290].strip()
EAC19 = line[290:297].strip()
EAC20 = line[297:304].strip()
Record_Axis_Conditions = line[340:342]
RA1 = line[343:348].strip()
RA2 = line[348:353].strip()
RA3 = line[353:358].strip()
RA4 = line[358:363].strip()
RA5 = line[363:368].strip()
RA6 = line[368:373].strip()
RA7 = line[373:378].strip()
RA8 = line[378:383].strip()
RA9 = line[383:388].strip()
RA10 = line[388:393].strip()
RA11 = line[393:398].strip()
RA12 = line[398:403].strip()
RA13 = line[403:408].strip()
RA14 = line[408:413].strip()
RA15 = line[413:418].strip()
RA16 = line[418:423].strip()
RA17 = line[423:428].strip()
RA18 = line[428:433].strip()
RA19 = line[433:438].strip()
RA20 = line[438:443].strip()'''
'''these values are not used'''

'''Race = line[444:446].strip()'''
race = {1: 'White',
2: 'Black',
3: 'American Indian (includes Aleuts and Eskimos)',
4: 'Chinese',
5: 'Japanese',
6: 'Hawaiian (includes Part-Hawaiian)',
7: 'Filipino',
18: 'Asian Indian',
28: 'Korean',
38: 'Samoan',
48: 'Vietnamese',
58: 'Guamanian',
68: 'Other Asian or Pacific Islander in areas reporting codes 18-58',
78: 'Combined other Asian or Pacific Islander, includes codes 18-68'}


'''Race_Bridged = line[446].strip()
Race_Imputation = line[447].strip()
Race_Recode_3 = line[448].strip()
Race_Recode_5 = line[449].strip()
Hispanic_Origin = line[483:486].strip()
Hispanic_Origin_Recode = line[487].strip()'''


################################################################
##              New columns
################################################################

def education(value):
    '''
    takes values as string and returns int
    meaning of values are in education dictionary
    '''
    if value == ' ':
        return 99
    elif value in [' 0','0']:
        return 0
    elif value in [' 06','6']:
        return 6
    elif value in [' 07','7']:
        return 7
    elif value in [' 08', '8']:
        return 8
    elif value in [' 09','9']:
        return 9
    elif value in [' 10','10']:
        return 10
    elif value in [' 11','11']:
            return 11
    elif value in [' 12', '12']:
        return 12
    elif value in [' 13','13']:
        return 13
    elif value in [' 14', '14']:
        return 14
    elif value in [' 15', '15']:
        return 15
    elif value in [' 16','16']:
            return 16
    elif value in [' 17', '17']:
        return 17
    elif value in [' 99','99']:
        return 99
    elif value ==' 15':
        return 15
    else:
        return value

def month_of_death(value):
    '''
    takes values as string and returns int 1 to 12
    meaning of values are in month_of_death dictionary (straightforward)
    '''
    if value in [101,102,103,104,105,106, 107, 108, 109]:
      return value%10
    elif value in [110, 111, 112]:
      return value-100
    else:
      return value

def Marital_Status_func(value):
    if value == ' S':
        return 1
    elif value == ' M':
        return 2
    elif value == ' D':
        return 3
    elif value == ' W':
        return 4
    elif value == ' U':
        return 5

def sex(value):
    '''
    returns 0 for male, 1 for female, 99 for unknown
    '''
    index = 0 #to count unknown gender
    if value == ' M':
      return 0
    elif value == ' F':
      return 1
    else:
      index += 1
      print '%d unknown gender'%index
      return 99

if __name__ == '__main__':
    print 'Loading the data set...'
    df_suicide = pd.read_csv('2013_suicide.csv')
    df_suicide['Education'] = df_suicide[' Education'].apply(education)
    print "Education column updated as 'Education'"
    df_suicide['Month_Of_Death'] = df_suicide[' Month_Of_Death'].apply(month_of_death)
    print "Month Of Death column updated as 'Month_of_Death'"
    df_suicide['DOW_of_Death'] = df_suicide[' DOW_of_Death'].apply(month_of_death)
    print "Day of Week Of Death column updated as 'DOW_of_Death'"
    df_suicide['Sex'] = df_suicide[' Sex'].apply(sex)
    print "Sex column updated as 'Sex'"
    df_suicide['Age'] = df_suicide[' Age_Value']
    print "Age column name change"
    df_suicide['Age_Groups'] = df_suicide[' Age_Recode_12']
    print "Age group column name change"
    df_suicide['Marital_Status'] = df_suicide[' Marital_Status'].apply(Marital_Status_func)
    print "Marital Status column name change"
    df_suicide['Place_Of_Death'] = df_suicide[' Place_Of_Death']
    print "Place_Of_Death column name change"
    df_suicide['Race'] = df_suicide[' Race']
    print "Race column name change"

    print ''
    print 'Dataset is available as df_suicide_clean;'
    print 'Dictionary list of all columns definition is available in dictionary_list;'
    print 'To see the order in which dictinary are stored, see dictionary_list_names'
    print 'To use, chose dictionary, ditionary keys are the various values of the column.'

    column_list = ['Resident_Status','Education','Month_Of_Death', 'DOW_of_Death', 'Sex',
            'Age', 'Age_Groups', 'Marital_Status', 'Place_Of_Death', 'Race']

    df_suicide_clean = df_suicide[column_list]
    dictionary_list_names = ['Resident_Status','Education','Month_Of_Death', 'DOW_of_Death', 'Sex',
             'Age_Groups', 'Marital_Status', 'Place_Of_Death', 'Race']
    dictionary_list = [Resident, education, month_of_death, DOW, sex, Age_Recode_12,
                    marital_status, place_of_death, race]
