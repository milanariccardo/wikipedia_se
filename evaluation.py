# -*- coding: utf-8 -*-
"""
@author: franc, Ricc
"""
import re
import os
import numpy as np
import pylab as pl
import math


#Crea insieme
def crea_insieme(nome):
    completeName = os.path.join(os.path.join(os.getcwd(),"Risultati"),nome+".txt")
    insieme = []
    try:
        file = open(completeName,"r")
        lines = file.readlines()
        for i in lines:
            insieme.append(i.rstrip())
    except IOError:
        print(completeName)
        print ("Error: File does not appear to exist.")
    return insieme

def dim_intersection(lst1, lst2):
    return len(set(lst1) & set(lst2))

def precision(dim_inter,dim_ans):
    return dim_inter/dim_ans

def recall(dim_inter, dim_ril):
    return dim_inter/dim_ril

def num_pos(array, x):
    dim = len(array)
    count_x = 0
    count_doc = 0
    i = 0
    while (count_x != x):
        if(i >= dim):
            return 0
        if(array[i] == 1):
            count_x = count_x + 1
        count_doc = count_doc + 1
        i = i + 1
    return count_doc

def precision_recall_level(ans,ril):
    dim_ans = len(ans)
    rilevanza_ans = []
    for i in  range(0,dim_ans):
        if ans[i] in ril:
            rilevanza_ans.append(1)
        else:
            rilevanza_ans.append(0)
    precision = [0,0,0,0,0,0,0,0,0,0]
    for t in range(0,10):
        temp = num_pos(rilevanza_ans,t+1)
        if(temp == 0):
            precision[t] = 0
        else:
            precision[t] = (t+1)/temp
    return precision


def avarage_precision(ans, ril):
    non_zero_count = 0
    precision = precision_recall_level(ans,ril)
    somma = 0
    dimensione = len(precision)
    for i in range(0,dimensione):
        if precision[i] != 0:
            non_zero_count = non_zero_count + 1
            somma = somma + precision[i]
    if non_zero_count == 0:
        return 0
    return somma/non_zero_count


def avarage_precision_all_query(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30):
    avg_all_query = []
    s = 0
    for i in range (0,10):
        s = a1[i]+a2[i]+a3[i]+a4[i]+a5[i]+a6[i]+a7[i]+a8[i]+a9[i]+a10[i]+a11[i]+a12[i]+a13[i]+a14[i]+a15[i]+a16[i]+a17[i]+a18[i]+a19[i]+a20[i]+a21[i]+a22[i]+a23[i]+a24[i]+a25[i]+a26[i]+a27[i]+a28[i]+a29[i]+a30[i]
        avg_all_query.append(s/30)
    return avg_all_query


def calcolo_log(peso, index):
    log = math.log(index, 2)
    return peso/log

pesi = [6,5,4,3,2,1,1,1,1,1]
iDCG = 17.578
nDCG = []

def NDCG(our_query, google_query):
    DCG = 0
    for i, our_result in enumerate(our_query):
        for j, google_result in enumerate(google_query):
            if (our_result == google_result):
                if(i == 0):
                    DCG = DCG + pesi[j]
                else:
                    DCG = DCG + calcolo_log(pesi[j], (i+1))
    nDCG.append(DCG/iDCG)


if ( __name__ == "__main__"):

    iDNA = ['DNA', 'Molecular models of DNA', 'A-DNA', 'RNA', 'DNA disambiguation',' Nucleic acid double helix', 'Nuclear DNA', 'DNA computing', 'Nucleic acid', 'Category DNA']
    iApple = ['Apple Inc.', 'History of Apple Inc.', 'Apple', 'Timeline of Apple Inc. products', 'List of mergers and acquisitions by Apple','Outline of Apple Inc.', 'Apple I', 'Apple disambiguation', 'Criticism of Apple Inc.','List of Apple operating systems']
    iEpigenetics = ['Epigenetics','Behavioral epigenetics','Cancer epigenetics','Transgenerational epigenetic inheritance','Epigenetics of human development','Epigenetics of schizophrenia','Epigenetics of physical exercise','Epigenetics in learning and memory','Computational epigenetics','Category Epigenetics']
    iHollywood = ['Hollywood', 'Cinema of the United States', 'Hollywood disambiguation', 'Hollywood Sign', 'New Hollywood', 'Wiktionary Hollywood', 'Hollywood 1923 film', 'Hollywood Hills', 'Hollywood North', 'Hollywood 2002 film']
    iMaya = ['Maya civilization', 'List of Maya sites', 'Maya peoples', 'Classic Maya collapse', 'Maya city', 'Maya', 'Autodesk Maya', 'Maya religion', 'Maya script', 'Maya given name']
    iMicrosoft = ['Microsoft', 'History of Microsoft', 'List of Microsoft software', 'United States v. Microsoft Corp.', 'Microsoft Store', 'List of mergers and acquisitions by Microsoft', 'Timeline of Microsoft', 'Microsoft Windows', 'Microsoft Live', 'Microsoft engineering groups']
    iPrecision = ['Precision', 'Precision and recall', 'F1 score', 'Positive and negative predictive values', 'Information retrieval', 'Relevance', 'Accuracy and precision', 'Precision computer science', 'Precision statistics', 'Talk Accuracy and precision']
    iTuscany = ['Tuscany', 'History of Tuscany', 'Category Tuscany', 'March of Tuscany', 'Category People from Tuscany', 'Tuscan wine', 'Grand Duchy of Tuscany', 'Category Provinces of Tuscany', 'Tuscany disambiguation', 'Tuscan dialect']
    i99_Balloons = ['99 Luftballons', '99 Luftballons album', 'Nena album', 'Nena band', 'Nena', 'Talk 99 Luftballons', 'Red Balloon', 'Carlo Karges', 'Jörn-Uwe Fahrenkrog-Petersen', 'Kevin McAlea']
    iComputer_programming = ['Computer programming', 'Portal Computer programming', 'Category Computer programming', 'Programming tool', 'Computer program', 'b Computer Programming', 'Programmer', 'Programming language', 'Outline of computer programming', 'Computer code']
    iFinancial_meltdown = ['Financial crisis', 'Financial crisis of 2007–08', 'Global financial system', 'Lehman Brothers', 'Subprime lending', 'European debt crisis', 'Great Recession', 'List of economic crises', 'Subprime mortgage crisis', 'Baring crisis']
    iJustin_timberlake = ['Justin Timberlake', 'Justin Timberlake discography', 'Justin Timberlake videography', 'Jessica Biel', 'List of songs recorded by Justin Timberlake', 'Cabaret Justin Timberlake song', 'Man of the Woods', 'Justified album', 'Category Albums produced by Justin Timberlake', 'NSYNC']
    iLeast_squares = ['Least squares', 'Linear least squares', 'Ordinary least squares', 'Regularized least squares', 'Category Least squares', 'Total least squares', 'Non-linear least squares', 'Numerical methods for linear least squares', 'Generalized least squares', 'Robust regression']
    iMars_robots = ['Mars rover', 'List of artificial objects on Mars', 'Crewed Mars rover', 'Category Mars rovers', 'Mars Exploration Rover', 'Curiosity rover', 'Opportunity rover', 'Comparison of embedded computer systems on board the Mars rovers', 'Exploration of Mars', 'Spirit rover']
    iPage_six = ['New York Post', 'Page 6', 'Richard Johnson columnist', 'Elizabeth Wagmeister', 'Bevy Smith', 'DailyFill', 'Claudia Cohen', 'Jared Paul Stern', 'James Brady columnist', 'Guest of a Guest']
    iRoman_empire = ['History of the Roman Empire', 'Ancient Rome', 'Roman Empire disambiguation', 'Fall of the Western Roman Empire', 'Holy Roman Empire', 'Western Roman Empire', 'Roman emperor', 'List of Roman emperors', 'Roman Empire TV series', 'Roman province']
    iSolar_energy = ['Solar energy', 'Solar power', 'Outline of solar energy', 'Solar Energy journal', 'Solar thermal energy', 'Solar panel', 'Solar power in Italy', 'Photovoltaics', 'Solar energy conversion', 'Solar power by country']
    iStatistical_significance = ['Statistical significance', 'P-value', 'Statistical hypothesis testing', 'Power statistics', 'Talk Statistical significance', 'Data dredging', 'Statistics', 'Analysis of variance', 'Confidence interval', 'Multiple comparisons problem']
    iSteve_Jobs = ['Steve Jobs', 'Steve Jobs film', 'Steve Jobs book', 'Laurene Powell Jobs', 'Chrisann Brennan', 'q Steve Jobs', 'Steve Wozniak', 'Category Steve Jobs', 'NeXT', 'Jobs film']
    iThe_maya = ['Maya civilization', 'History of the Maya civilization', 'List of Maya sites', 'Maya city', 'Maya peoples', 'Maya architecture', 'Maya', 'Maya astronomy', 'Wikipedia WikiProject WikiFundi Content/Maya civilization', 'Ancient Maya art']
    iTriple_cross = ['Triple Cross 1966 film', 'Triple Cross', 'The Triple Cross', 'Triple product', 'Joe Palooka in Triple Cross', 'Papal cross', 'Eddie Chapman', 'Dagmar Lahlum', 'Burnopfield', 'Ronnie Reed']
    iUS_Consitution = ['Constitution of the United States', 'List of amendments to the United States Constitution', 'Article One of the United States Constitution', 'History of the United States Constitution', 's Constitution of the United States of America', 'Article Two of the United States Constitution', 'Preamble to the United States Constitution', 'Constitution', 'Article Five of the United States Constitution', 'Article Four of the United States Constitution']
    iEye_of_Horus = ['Eye of Horus', 'Eye of Ra', 'Eye of Horus video game', 'Rhind Mathematical Papyrus', 'Talk Eye of Horus', 'Litany of the Eye of Horus', 'Horus', 'Four sons of Horus', 'The Contendings of Horus and Seth', 'Ihy']
    iMadam_Im_Adam = ['Palindrome', 'Madam Adam', 'The Palindromist', 'Mark Saltveit', 'Young and Rich', 'Call Me Madam', 'Dax Jordan', 'What Do You Want from Live', 'Deborah Jeane Palfrey', 'Call Me Madam film']
    iMean_average_precision = ['Evaluation measures information retrieval', 'Mean reciprocal rank', 'Precision and recall', 'Information retrieval', 'Mean absolute percentage error', 'F1 score', 'Learning to rank', 'Accuracy and precision', 'Human-computer information retrieval', 'Mean absolute error']
    iPhysics_nobel_prizes = ['List of Nobel laureates in Physics', 'Lawrence Bragg', 'Shuji Nakamura', 'David J. Thouless', 'Nobel Prize in Physics', 'List of Nobel laureates', 'Nobel Prize', 'List of Nobel laureates by country', 'Nobel Committee for Physics', 'Ig Nobel Prize']
    iRead_the_manual = ['RTFM', 'Owner\'s manual', 'Talk RTFM', 'Owner\'s Manual TV series', 'The Manual', 'Autonomous spaceport drone ship', 'User guide', 'Wikipedia Simplified Manual of Style', 'Talk Hit Man manual', 'Quickstart guide']
    iSpanish_civil_war = ['Spanish Civil War', '1936 in the Spanish Civil War', '1938-39 in the Spanish Civil War', 'Nationalist faction Spanish Civil War', 'Foreign involvement in the Spanish Civil War', 'Republican faction Spanish Civil War', 'Final offensive of the Spanish Civil War', 'Category Spanish Civil War', 'Background of the Spanish Civil War', 'Siege of Madrid']
    iDo_geese_see_god = ['The Palindromist', 'Palindrome', 'David Slade', 'Talk Palindrome', 'The Wind band', 'Tengri', 'Hamsa bird', 'Dave Seaman', 'Ania Marson', 'Greylag goose']
    iMuch_ado_about_nothing = ['Much Ado About Nothing', 'Much Ado About Nothing 1993 film', 'Much Ado About Nothing 2012 film', 'Much Ado About Nothing opera', 'Much Ado About Nothing disambiguation', 'Don Pedro Much Ado About Nothing', 'Much Ado About Nothing 1973 film', 'Template Much Ado About Nothing', 'Much Ado', 'Talk Much Ado About Nothing']



    DNA = crea_insieme("DNA")
    Apple = crea_insieme("Apple")
    Epigenetics = crea_insieme("Epigenetics")
    Hollywood = crea_insieme("Hollywood")
    Maya = crea_insieme("Maya")
    Microsoft = crea_insieme("Microsoft")
    Precision = crea_insieme("Precision")
    Tuscany = crea_insieme("Tuscany")
    insime_99_Balloons = crea_insieme("99_balloons")
    Computer_programming = crea_insieme("Computer_Programming")
    Financial_meltdown =  crea_insieme("Financial_meltdown")
    Justin_timberlake =  crea_insieme("Justin_Timberlake")
    Least_squares =  crea_insieme("Least_Squares")
    Mars_robots =  crea_insieme("Mars_robots")
    Page_six =  crea_insieme("Page_six")
    Roman_empire =  crea_insieme("Roman_Empire")
    Solar_energy =  crea_insieme("Solar_energy")
    Statistical_significance =  crea_insieme("Statistical_Significance")
    Steve_Jobs =  crea_insieme("Steve_Jobs")
    The_maya =  crea_insieme("The_Maya")
    Triple_cross =  crea_insieme("Triple_Cross")
    US_Consitution =  crea_insieme("US_Constitution")
    Eye_of_Horus =  crea_insieme("Eye_of_Horus")
    Madam_Im_Adam =  crea_insieme("Madam_I’m_Adam")
    Mean_average_precision =  crea_insieme("Mean_Average_Precision")
    Physics_nobel_prizes =  crea_insieme("Physics_Nobel_Prizes")
    Read_the_manual =  crea_insieme("Read_the_manual")
    Spanish_civil_war =  crea_insieme("Spanish_Civil_War")
    Do_geese_see_god =  crea_insieme("Do_geese_see_god")
    Much_ado_about_nothing =  crea_insieme("Much_ado_about_nothing")

    ''' Livelli di recall-precision '''
    prec_lev_recDNA = precision_recall_level(DNA,iDNA)
    prec_lev_recApple = precision_recall_level(Apple,iApple)
    prec_lev_recEpigenetics = precision_recall_level(Epigenetics,iEpigenetics)
    prec_lev_recHollywood = precision_recall_level(Hollywood,iHollywood)
    prec_lev_recMaya = precision_recall_level(Maya,iMaya)
    prec_lev_recMicrosoft = precision_recall_level(Microsoft,iMicrosoft)
    prec_lev_recPrecision = precision_recall_level(Precision,iPrecision)
    prec_lev_recTuscany = precision_recall_level(Tuscany,iTuscany)
    prec_lev_recpinsime_99_Balloons = precision_recall_level(insime_99_Balloons,i99_Balloons)
    prec_lev_recpComputer_programming = precision_recall_level(Computer_programming,iComputer_programming)
    prec_lev_recpFinancial_meltdown = precision_recall_level(Financial_meltdown,iFinancial_meltdown)
    prec_lev_recpJustin_timberlake = precision_recall_level(Justin_timberlake,iJustin_timberlake)
    prec_lev_recLeast_squares = precision_recall_level(Least_squares,iLeast_squares)
    prec_lev_recMars_robots = precision_recall_level(Mars_robots,iMars_robots)
    prec_lev_recPage_six = precision_recall_level(Page_six,iPage_six)
    prec_lev_recRoman_empire = precision_recall_level(Roman_empire,iRoman_empire)
    prec_lev_recSolar_energy = precision_recall_level(Solar_energy,iSolar_energy)
    prec_lev_recStatistical_significance = precision_recall_level(Statistical_significance,iStatistical_significance)
    prec_lev_recSteve_Jobs = precision_recall_level(Steve_Jobs,iSteve_Jobs)
    prec_lev_recThe_maya = precision_recall_level(The_maya,iThe_maya)
    prec_lev_recTriple_cross = precision_recall_level(Triple_cross,iTriple_cross)
    prec_lev_recUS_Consitution = precision_recall_level(US_Consitution,iUS_Consitution)
    prec_lev_recEye_of_Horus = precision_recall_level(Eye_of_Horus,iEye_of_Horus)
    prec_lev_recMadam_Im_Adam = precision_recall_level(Madam_Im_Adam,iMadam_Im_Adam)
    prec_lev_recMean_average_precision = precision_recall_level(Mean_average_precision,iMean_average_precision)
    prec_lev_recPhysics_nobel_prizes = precision_recall_level(Physics_nobel_prizes,iPhysics_nobel_prizes)
    prec_lev_recRead_the_manual = precision_recall_level(Read_the_manual,iRead_the_manual)
    prec_lev_recSpanish_civil_war = precision_recall_level(Spanish_civil_war,iSpanish_civil_war)
    prec_lev_recDo_geese_see_god = precision_recall_level(Do_geese_see_god,iDo_geese_see_god)
    prec_lev_recMuch_ado_about_nothing = precision_recall_level(Much_ado_about_nothing,iMuch_ado_about_nothing)


    ''' Avarage precision '''
    avgpDNA = avarage_precision(DNA,iDNA)
    avgpApple = avarage_precision(Apple,iApple)
    avgpEpigenetics = avarage_precision(Epigenetics,iEpigenetics)
    avgpHollywood = avarage_precision(Hollywood,iHollywood)
    avgpMaya = avarage_precision(Maya,iMaya)
    avgpMicrosoft = avarage_precision(Microsoft,iMicrosoft)
    avgpPrecision = avarage_precision(Precision,iPrecision)
    avgpTuscany = avarage_precision(Tuscany,iTuscany)
    avgppinsime_99_Balloons = avarage_precision(insime_99_Balloons,i99_Balloons)
    avgppComputer_programming = avarage_precision(Computer_programming,iComputer_programming)
    avgppFinancial_meltdown = avarage_precision(Financial_meltdown,iFinancial_meltdown)
    avgppJustin_timberlake = avarage_precision(Justin_timberlake,iJustin_timberlake)
    avgpLeast_squares = avarage_precision(Least_squares,iLeast_squares)
    avgpMars_robots = avarage_precision(Mars_robots,iMars_robots)
    avgpPage_six = avarage_precision(Page_six,iPage_six)
    avgpRoman_empire = avarage_precision(Roman_empire,iRoman_empire)
    avgpSolar_energy = avarage_precision(Solar_energy,iSolar_energy)
    avgpStatistical_significance = avarage_precision(Statistical_significance,iStatistical_significance)
    avgpSteve_Jobs = avarage_precision(Steve_Jobs,iSteve_Jobs)
    avgpThe_maya = avarage_precision(The_maya,iThe_maya)
    avgpTriple_cross = avarage_precision(Triple_cross,iTriple_cross)
    avgpUS_Consitution = avarage_precision(US_Consitution,iUS_Consitution)
    avgpEye_of_Horus = avarage_precision(Eye_of_Horus,iEye_of_Horus)
    avgpMadam_Im_Adam = avarage_precision(Madam_Im_Adam,iMadam_Im_Adam)
    avgpMean_average_precision = avarage_precision(Mean_average_precision,iMean_average_precision)
    avgpPhysics_nobel_prizes = avarage_precision(Physics_nobel_prizes,iPhysics_nobel_prizes)
    avgpRead_the_manual = avarage_precision(Read_the_manual,iRead_the_manual)
    avgpSpanish_civil_war = avarage_precision(Spanish_civil_war,iSpanish_civil_war)
    avgpDo_geese_see_god = avarage_precision(Do_geese_see_god,iDo_geese_see_god)
    avgpMuch_ado_about_nothing = avarage_precision(Much_ado_about_nothing,iMuch_ado_about_nothing)

    ''' Copia nel file '''

    file = open("Avarage_precision.txt","w")
    file.write("%0.3f\n" % avgpDNA)
    file.write("%0.3f\n" % avgpApple)
    file.write("%0.3f\n" % avgpEpigenetics)
    file.write("%0.3f\n" % avgpHollywood)
    file.write("%0.3f\n" % avgpMaya)
    file.write("%0.3f\n" % avgpMicrosoft)
    file.write("%0.3f\n" % avgpPrecision)
    file.write("%0.3f\n" % avgpTuscany)
    file.write("%0.3f\n" % avgppinsime_99_Balloons)
    file.write("%0.3f\n" % avgppComputer_programming)
    file.write("%0.3f\n" % avgppFinancial_meltdown)
    file.write("%0.3f\n" % avgppJustin_timberlake)
    file.write("%0.3f\n" % avgpLeast_squares)
    file.write("%0.3f\n" % avgpMars_robots)
    file.write("%0.3f\n" % avgpPage_six)
    file.write("%0.3f\n" % avgpRoman_empire)
    file.write("%0.3f\n" % avgpSolar_energy)
    file.write("%0.3f\n" % avgpStatistical_significance)
    file.write("%0.3f\n" % avgpSteve_Jobs)
    file.write("%0.3f\n" % avgpThe_maya)
    file.write("%0.3f\n" % avgpTriple_cross)
    file.write("%0.3f\n" % avgpUS_Consitution)
    file.write("%0.3f\n" % avgpEye_of_Horus)
    file.write("%0.3f\n" % avgpMadam_Im_Adam)
    file.write("%0.3f\n" % avgpMean_average_precision)
    file.write("%0.3f\n" % avgpPhysics_nobel_prizes)
    file.write("%0.3f\n" % avgpRead_the_manual)
    file.write("%0.3f\n" % avgpSpanish_civil_war)
    file.write("%0.3f\n" % avgpDo_geese_see_god)
    file.write("%0.3f\n" % avgpMuch_ado_about_nothing)
    file.close()

    ''' Avarage precision su tutte le query '''
    avg_all_query = avarage_precision_all_query(prec_lev_recDNA,prec_lev_recApple, prec_lev_recEpigenetics , prec_lev_recHollywood ,prec_lev_recMaya ,prec_lev_recMicrosoft ,prec_lev_recPrecision ,prec_lev_recTuscany ,prec_lev_recpinsime_99_Balloons ,prec_lev_recpComputer_programming ,prec_lev_recpFinancial_meltdown ,prec_lev_recpJustin_timberlake ,prec_lev_recLeast_squares ,prec_lev_recMars_robots ,prec_lev_recPage_six ,prec_lev_recRoman_empire ,prec_lev_recSolar_energy ,prec_lev_recStatistical_significance ,prec_lev_recSteve_Jobs ,prec_lev_recThe_maya ,prec_lev_recTriple_cross ,prec_lev_recUS_Consitution ,prec_lev_recEye_of_Horus ,prec_lev_recMadam_Im_Adam ,prec_lev_recMean_average_precision ,prec_lev_recPhysics_nobel_prizes ,prec_lev_recRead_the_manual ,prec_lev_recSpanish_civil_war ,prec_lev_recDo_geese_see_god ,prec_lev_recMuch_ado_about_nothing)

    ''' Calcolo della MAP '''
    MAP = (avgpDNA +avgpApple +avgpEpigenetics +avgpHollywood +avgpMaya +avgpMicrosoft +avgpPrecision +avgpTuscany +avgppinsime_99_Balloons +avgppComputer_programming +avgppFinancial_meltdown +avgppJustin_timberlake +avgpLeast_squares +avgpMars_robots +avgpPage_six +avgpRoman_empire +avgpSolar_energy +avgpStatistical_significance +avgpSteve_Jobs +avgpThe_maya +avgpTriple_cross +avgpUS_Consitution +avgpEye_of_Horus +avgpMadam_Im_Adam +avgpMean_average_precision +avgpPhysics_nobel_prizes +avgpRead_the_manual +avgpSpanish_civil_war +avgpDo_geese_see_god +avgpMuch_ado_about_nothing)/30
    print("MAP %0.3f\n" % MAP)

    ''' Calcolo NDCG '''
    ndcDNA = NDCG(DNA,iDNA)
    ndcApple = NDCG(Apple,iApple)
    ndcEpigenetics = NDCG(Epigenetics,iEpigenetics)
    ndcHollywood = NDCG(Hollywood,iHollywood)
    ndcMaya = NDCG(Maya,iMaya)
    ndcMicrosoft = NDCG(Microsoft,iMicrosoft)
    ndcPrecision = NDCG(Precision,iPrecision)
    ndcTuscany = NDCG(Tuscany,iTuscany)
    ndcpinsime_99_Balloons = NDCG(insime_99_Balloons,i99_Balloons)
    ndcpComputer_programming = NDCG(Computer_programming,iComputer_programming)
    ndcpFinancial_meltdown = NDCG(Financial_meltdown,iFinancial_meltdown)
    ndcpJustin_timberlake = NDCG(Justin_timberlake,iJustin_timberlake)
    ndcLeast_squares = NDCG(Least_squares,iLeast_squares)
    ndcMars_robots = NDCG(Mars_robots,iMars_robots)
    ndcPage_six = NDCG(Page_six,iPage_six)
    ndcRoman_empire = NDCG(Roman_empire,iRoman_empire)
    ndcSolar_energy = NDCG(Solar_energy,iSolar_energy)
    ndcStatistical_significance = NDCG(Statistical_significance,iStatistical_significance)
    ndcSteve_Jobs = NDCG(Steve_Jobs,iSteve_Jobs)
    ndcThe_maya = NDCG(The_maya,iThe_maya)
    ndcTriple_cross = NDCG(Triple_cross,iTriple_cross)
    ndcUS_Consitution = NDCG(US_Consitution,iUS_Consitution)
    ndcEye_of_Horus = NDCG(Eye_of_Horus,iEye_of_Horus)
    ndcMadam_Im_Adam = NDCG(Madam_Im_Adam,iMadam_Im_Adam)
    ndcMean_average_precision = NDCG(Mean_average_precision,iMean_average_precision)
    ndcPhysics_nobel_prizes = NDCG(Physics_nobel_prizes,iPhysics_nobel_prizes)
    ndcRead_the_manual = NDCG(Read_the_manual,iRead_the_manual)
    ndcSpanish_civil_war = NDCG(Spanish_civil_war,iSpanish_civil_war)
    ndcDo_geese_see_god = NDCG(Do_geese_see_god,iDo_geese_see_god)
    ndcMuch_ado_about_nothing = NDCG(Much_ado_about_nothing,iMuch_ado_about_nothing)

    ''' Stampa grafico NDCG '''
    x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    pl.bar(x,nDCG)
    pl.show()

    ''' Stampa grafico avarage precision su tutte le query '''
    recall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pl.plot(recall, avg_all_query)              # Usa pylab per tracciare con  x,y
    pl.show()
