# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons
# source n 8
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.comaddon import  VSlog
import re
import string
import json

# selection bVSlog=True ou bVSlog=False
#bVSlog=True
bVSlog=False


SITE_IDENTIFIER = 'mystream_zone'
SITE_NAME = 'My Stream'
SITE_DESC = 'Regarder Films et Séries en Streaming gratuit'

URL_MAIN = 'https://mystream.zone/'

FUNCTION_SEARCH = 'showMovies'
URL_SEARCH = (URL_MAIN + '?s=', 'showMovies')

URL_SEARCH_MOVIES = (URL_SEARCH[0], 'showMovies')
URL_SEARCH_SERIES = (URL_SEARCH[0], 'showMovies')


MOVIE_MOVIES = (URL_MAIN+'movies/', 'showMovies')
MOVIE_GENRES = (True, 'showGenres')
MOVIE_ANNEES = (True, 'showYears')
MOVIE_ALPHA = (True, 'showAlphaMovies')
MOVIE_FEATURED = (URL_MAIN, 'showMovies')
#MOVIE_NEWS = (URL_MAIN + '/films/', 'showMovies')

SERIE_SERIES = (URL_MAIN+'tvshows/', 'showMovies')
SERIE_ALPHA = (True, 'showAlphaSeries')

SERIE_NEWS_SAISONS = (URL_MAIN + 'seasons/', 'showMovies')
SERIE_NEWS_EPISODES= (URL_MAIN + 'episodes/', 'showMovies')

# a faire
MOVIE_TOP_IMD=(URL_MAIN + 'imdb/', 'showMovies') 
SERIE_TOP_IMD=(URL_MAIN + 'imdb/', 'showMovies') 
MOVIE_TENDANCE='https://mystream.zone/tendance/'

def load():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Recherche', 'search.png', oOutputParameterHandler)

    #oOutputParameterHandler = cOutputParameterHandler()
    #oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    #oGui.addDir(SITE_IDENTIFIER, 'showMenuMovies', 'Films', 'films.png', oOutputParameterHandler)

    #oOutputParameterHandler = cOutputParameterHandler()
    #oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    #oGui.addDir(SITE_IDENTIFIER, 'showMenuSeries', 'Séries', 'series.png', oOutputParameterHandler)
     
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_GENRES[1], 'Films & Series (Par Genres)', 'genres.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_ANNEES[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_ANNEES[1], 'Films & Series (Par années)', 'annees.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_MOVIES[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_MOVIES[1], 'Films ', 'films.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_FEATURED[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_FEATURED[1], 'Films (En vedette)', 'star.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_ALPHA[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_ALPHA[1], 'Films (Ordre alphabétique)', 'listes.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_SERIES[1], 'Séries ', 'series.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_NEWS_SAISONS[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS_SAISONS[1], 'Séries (Saisons récentes)', 'news.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_NEWS_EPISODES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS_EPISODES[1], 'Séries (Episodes Recents)', 'news.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_ALPHA[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_ALPHA[1], 'Séries (Ordre alphabétique)', 'listes.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()
    
    oGui.setEndOfDirectory()


def showMenuMovies():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_MOVIES[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_MOVIES[1], 'Films ', 'films.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_FEATURED[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_FEATURED[1], 'Films (En vedette)', 'star.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_ALPHA[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_ALPHA[1], 'Films (Ordre alphabétique)', 'listes.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showMenuSeries():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_SERIES[1], 'Séries ', 'series.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_NEWS_SAISONS[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS_SAISONS[1], 'Séries (Saisons récentes)', 'news.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_NEWS_EPISODES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS_EPISODES[1], 'Séries (Episodes Recents)', 'news.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_ALPHA[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_ALPHA[1], 'Séries (Ordre alphabétique)', 'listes.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()


def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = URL_SEARCH[0] + sSearchText.replace(' ', '%20')
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return

def showGenres():
    oGui = cGui()
    sUrl =URL_MAIN
    #https://mystream.zone/genre/action/    /genre//
    liste = []
    liste.append(['Action', sUrl + 'genre/action/'])
    liste.append(['Action & Adventure', sUrl + 'genre/action-adventure/'])
    liste.append(['Adventure', sUrl + 'genre/adventure/'])
    liste.append(['Aventure', sUrl + 'genre/aventure/'])
    liste.append(['Animation', sUrl + 'genre/animation/'])
    liste.append(['Aventure', sUrl + 'genre/aventure/'])
    liste.append(['Comedie', sUrl + 'genre/comedie/'])
    liste.append(['Comedy', sUrl + 'genre/comedie/'])
    liste.append(['Crime', sUrl + 'genre/crime/'])
    liste.append(['Documentaire', sUrl + 'genre/documentaire/'])
    liste.append(['Documentary', sUrl + 'genre/documentary/'])
    liste.append(['Drama', sUrl + 'genre/drama/'])
    liste.append(['Drame', sUrl + 'genre/drame/'])
    liste.append(['Familial', sUrl + 'genre/familial/'])
    liste.append(['Family', sUrl + 'genre/family/'])
    liste.append(['Fantastique', sUrl + 'genre/fantastique/'])
    liste.append(['Fantasy', sUrl + 'genre/fantasy/'])
    liste.append(['Guerre', sUrl + 'genre/guerre/'])
    liste.append(['Histoire', sUrl + 'genre/histoire/'])
    liste.append(['History', sUrl + 'genre/history/'])
    liste.append(['Horreur', sUrl + 'genre/horreur/'])
    liste.append(['Horror', sUrl + 'genre/horror/'])
    liste.append(['Kids', sUrl + 'genre/kids/'])
    liste.append(['Music', sUrl + 'genre/music/'])
    liste.append(['Musique', sUrl + 'genre/musique/'])
    liste.append(['Mystère', sUrl + 'genre/mystere/'])
    liste.append(['Mystery', sUrl + 'genre/mystery/'])
    liste.append(['Reality', sUrl + 'genre/reality/'])
    liste.append(['Romance', sUrl + 'genre/romance/'])
    liste.append(['Sci-Fi & Fantasy', sUrl + 'genre/sci-fi-fantasy/'])
    liste.append(['Sci-Fi', sUrl + 'genre/science-fiction/'])
    liste.append(['Sci-Fi & Fantastique' , sUrl + 'genre/science-fiction-fantastique/'])
    liste.append(['Soap', sUrl + 'genre/soap/'])
    liste.append(['Talk', sUrl + 'genre/talk/'])
    liste.append(['Telefilm', sUrl + 'genre/telefilm/'])
    liste.append(['Thriller', sUrl + 'genre/thriller/'])
    liste.append(['Tv Movie', sUrl + 'genre/tv-movie/'])
    liste.append(['Guerre', sUrl + 'genre/war/'])
    liste.append(['Guerre & politique', sUrl + 'genre/sci-fi-fantasy/'])
    
    for sTitle, sUrlgenre in liste:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrlgenre)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()


def showAlphaMovies():
    showAlpha('movies')
    
def showAlphaSeries() :
    showAlpha('tvshows')
    
def showAlpha(stype):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    #requete json 20 resultat max
    #https://mystream.zone/wp-json/dooplay/glossary/?term=g&nonce=2132c17353&type=tvshows
    url1='https://mystream.zone/wp-json/dooplay/glossary/?term='
    url2='&nonce='
    snonce='2132c17353'  # a surveiller si jamais cela change
    url3='&type='

    sAlpha= string.ascii_lowercase
    listalpha = list(sAlpha)
    liste = []
    for alpha in listalpha :
        liste.append([str(alpha).upper(),url1+str(alpha) + url2 + snonce +url3+stype])

    for sTitle, sUrl in liste:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Lettre [COLOR coral]' + sTitle + '[/COLOR]', 'listes.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showYears():
    oGui = cGui()
    #https://mystream.zone/release/2020
    for i in reversed(range(1982, 2021)):
        sYear = str(i)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + 'release/' + sYear)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sYear, 'annees.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showMovies(sSearch=''):
    oGui = cGui()
    oParser = cParser()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    if sSearch:
        sUrl = sSearch.replace(' ', '%20')   
    
    #VSlog('url request=' + sUrl)
 
    if 'wp-json' in sUrl and not sSearch:
        oRequestHandler = cRequestHandler(sUrl) 
        sJsonContent = oRequestHandler.request()
        jsonrsp  = json.loads(sJsonContent)
        
        ifVSlog(str(jsonrsp ))
        for i, idict in jsonrsp.items():    
            sTitle=str(jsonrsp[i]['title'].encode('utf-8', 'ignore'))  #I Know This Much Is True mystream
            sUrl2=str(jsonrsp[i]['url'])
            sThumb=str(jsonrsp[i]['img'])
            sYears=str(jsonrsp[i]['year'])
            #VSlog('response url2 '+ sUrl2)
            sDisplayTitle = sTitle + ' (' + sYears + ')'
            sDesc = ''
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sYears', sYears)
        
            if 'type=tvshows' in sUrl:
                oGui.addTV(SITE_IDENTIFIER, 'showSaisons', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)
        
        #  1 result with <= 20 items
        oGui.setEndOfDirectory()
        return
    #A faire
    #https://mystream.zone/tendance/ 
    #url name years immage
    if 'https://mystream.zone/tendance/' in sUrl:
        sPattern = 'class="mepo">.+?class=.data.+?href="([^"]*).+?([^<]*).+?span>.+?,.([^<]*).+?src="([^"]*)'

    #https://mystream.zone/ Feature movie 8 resultats
    #url image title
    elif sUrl=='https://mystream.zone/':
        sPattern = 'data dfeatur.+?href="([^"]*)".+?src="([^"]*).+?alt="([^"]*)'
        
    #https://mystream.zone/seasons/
    #image  url   number title 
    #elif sUrl=='https://mystream.zone/saisons/':
    elif 'https://mystream.zone/seasons/' in sUrl: 
        sPattern = 'item se seasons.+?src="([^"]*)".+?href="([^"]*).+?class="b">([^<]*).+?c">([^<]*)'
    
    #https://mystream.zone/episodes/
    #url 'S1.E1.'  years '.2020'   title img
    elif 'https://mystream.zone/episodes/' in sUrl:
        sPattern = 'div class="season_m.+?data.+?href="([^"]*)"..+?span>([^\/]*).+?,([^<]*).+?serie">([^<]*).+?src="([^"]*)"'
    
    #url search https://mystream.zone/?s=
    elif 'https://mystream.zone/?s=' in sUrl :# thumb url title years desc
        sPattern = 'animation-2.+?img src="([^"]*).+?class="title.+?ref="([^"]*)".([^<]*).+?year">([^<]*).*?contenido.><p>([^<]*)'
                
    elif 'action' or 'tvshows'  or 'movies'or 'release' in sUrl :
        #bug image premiere image page ;pattern non resolu
        #sPattern = 'class="mepo">.+?class=.data.+?href="([^"]*).>([^<]*).+?span>.+?,.([^<]*).+?texto">([^<]*).+?src="([^"]*)"'
        #sPattern ='class="item movies.+?src="([^"]*).+?class="mepo">.+?class="data".+?href="([^"]*).>([^<]*).+?span>.+?,.([^<]*).+?texto">([^<]*)'
        #thumb url title years desc bug 1 er match thumb 
        sPattern ='class="item.+?src="([^"]*).+?class="mepo">.+?class="data".+?href="([^"]*).>([^<]*).+?span>.+?,.([^<]*).+?texto">([^<]*)' 
    
    else :
        ifVSlog('requete inconnue '+sUrl)
        oGui.setEndOfDirectory()
        return

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)
        
        ifVSlog(sHtmlContent)
        ifVSlog('')
        ifVSlog('Failed Pattern with url = '+sUrl )
        ifVSlog(sPattern )
     
    if (aResult[0] == True):
        sDesc = ''
        sYear = ''
        
        for aEntry in aResult[1]:
            ifVSlog('Result:')
           
            if 'https://mystream.zone/tendance/'in sUrl:#  url title years immage
                sUrl2 =aEntry[0]
                sTitle = aEntry[1]
                sThumb= aEntry[3]
                sDisplayTitle= sTitle + '('+ aEntry[2]  +')'
                  
            elif sUrl=='https://mystream.zone/': # url image title   
                sUrl2 =aEntry[0]
                sTitle = str(aEntry[2]).replace(' mystream', '')
                sThumb= aEntry[1]
                sDisplayTitle= sTitle 
                                
            elif  'https://mystream.zone/seasons/' in sUrl : #  image  url number title   
                sUrl2 =aEntry[1]
                sTitle = aEntry[3] 
                sThumb= aEntry[0]
                sDisplayTitle= sTitle + ' Saison ' + aEntry[2]
                
            elif 'https://mystream.zone/episodes/' in sUrl: # url ;'S1.E1.' ; years '.2020' ;  title; img
                sUrl2 =aEntry[0]
                sTitle = aEntry[3]  + ' ' + aEntry[1] 
                sThumb= aEntry[4]
                sDisplayTitle= sTitle  + '('+ aEntry[2]  +')'
                sYear= aEntry[2]
            
            elif 'https://mystream.zone/?s=' in sUrl :# img url title years desc
                sUrl2 =aEntry[1]
                sTitle = str(aEntry[2]).replace(' mystream', '')
                sThumb= aEntry[0]
                sDesc= aEntry[4]
                sYear= aEntry[3]
                sDisplayTitle= sTitle+ ' (' + sYear + ' )'

            else : # thumb url title years desc
                sUrl2 =aEntry[1]
                sTitle = str(aEntry[2]).replace(' mystream', '')
                sThumb= aEntry[0]
                sDesc= aEntry[4]
                sYear= aEntry[3]
                sDisplayTitle= sTitle + ' (' + sYear + ' )'   
            
            if sUrl2.startswith('/'):
                sUrl2 = URL_MAIN + sUrl2
            if sThumb.startswith('/'):
                sThumb = URL_MAIN + sThumb
            
            ifVSlog('name= '+ sTitle)
            ifVSlog('url= ' + sUrl2 )
            ifVSlog('sThumb= ' + sThumb )
            ifVSlog('desc= ' + sDesc )
            ifVSlog('syears= ' + sYear)
            
            if 'mystream.zone/release/' in sUrl or 'mystream.zone/genre/' in sUrl:
            
                ifVSlog('Try ADD tag Film or serie ')
                if 'movies' in sUrl2 :
                    sDisplayTitle= sTitle + ' ( Film )'
                    
                if 'tvshows' in sUrl2 :
                    sDisplayTitle= sTitle + ' ( Serie )'
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oOutputParameterHandler.addParameter('sYear', sYear)
            if 'mystream.zone/tvshows'  in sUrl2:
                ifVSlog('ADD TV ; showSaisons')
                oGui.addTV(SITE_IDENTIFIER, 'showSaisons', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)
            
            elif 'mystream.zone/seasons' in sUrl2 :
                ifVSlog('ADD TV ; showEpisodes')
                oGui.addTV(SITE_IDENTIFIER, 'showEpisodes', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)
            
            else:
                ifVSlog('ADD Movie ; showHosters')
                oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)
        
        bNextPage,urlNextpage,pagination  = __checkForNextPage(sHtmlContent)
        if (bNextPage):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', urlNextpage) 
            oGui.addNext(SITE_IDENTIFIER, 'showMovies', '[COLOR teal] ' + pagination + ' >>>[/COLOR]', oOutputParameterHandler)
    
    if not sSearch:  
        oGui.setEndOfDirectory()


def __checkForNextPage(sHtmlContent):
    oParser = cParser()
    bnext=False
    urlNextpage='no find'
    #note pas de class=.arrow dans la recherche
    #return false
    sPattern = 'class=.arrow.+?ref="([^"]*)"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):   
        urlNextpage=str(aResult[1][0])
        bnext=True     
    try:
        numberNext= re.search('page/([0-9]+)', urlNextpage).group(1)     
    except:
        numberNext=''
        pass
    
    sPattern = 'class="pagination"><span>([^<]*)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        pagination=aResult[1][0]
    try:
        NumberMax= re.search('([0-9]+)$', pagination).group(1)
    except:
        NumberMax=''
        pass
    
    if bnext :
        pagination=''
        if numberNext:
            pagination='Page ' + numberNext
        if NumberMax:
            pagination= pagination+'/'+NumberMax+' '
        return True ,urlNextpage, pagination
    else :
        ifVSlog('no find next page')
        return False ,urlNextpage, 'nothing'


def showSaisons():
    #parent https://mystream.zone/tvshows/
    oGui = cGui() 
    oInputParameterHandler = cInputParameterHandler()
    
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sDesc= oInputParameterHandler.getValue('sDesc')
    sTitle= oInputParameterHandler.getValue('sMovieTitle')
    sYear= oInputParameterHandler.getValue('sYear')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    oParser = cParser()
    #probleme:pas de liens existants vers les pages saisons
    #a faire ? ''
    if False:
        try:
            sPattern = 'Synopsis et détails:.+?treaming :([^<]+)<'
            aResult = oParser.parse(sHtmlContent, sPattern)
            if aResult[0]:
                sDesc = aResult[1][0]
        except:
            pass
    
    #  '2 - 11'   href   title
    #class='numerando'>([^<]*).+?href='([^']*).>([^<]*) #
    sPattern = "class='numerando'>([^<]*).+?href='([^']*)"
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        ListNumeroSaison=[]
        listeUrlEpisode=[]
        listeStitle=[]
        
        for aEntry in aResult[1]:
            ifVSlog(aEntry[0])
            iSaison = re.search('([0-9]+)', aEntry[0]).group(1)
            iEpisode= re.search('([0-9]+)$', aEntry[0]).group(1)
                
            if not str(iSaison) in ListNumeroSaison :
                ListNumeroSaison.append(str(iSaison))
                sTitleDisplay=sTitle +' '+ 'Saison' + ' '+ str(iSaison )
                if sYear:
                    sTitleDisplay= sTitleDisplay + ' (' + sYear + ' )' 
                
                if len(listeUrlEpisode) >0: 
                    ifVSlog('ADD showEpisodes')
                    oOutputParameterHandler = cOutputParameterHandler()
                    oOutputParameterHandler.addParameter('siteUrl', sUrl)
                    oOutputParameterHandler.addParameter('sThumb', sThumb)
                    oOutputParameterHandler.addParameter('sDesc', sDesc)
                    oOutputParameterHandler.addParameter('listeUrlEpisode', listeUrlEpisode)
                    oOutputParameterHandler.addParameter('listeStitle', listeStitle)
                    oOutputParameterHandler.addParameter('sYear', sYear)
                    oGui.addTV(SITE_IDENTIFIER, 'showListEpisodes', sTitleDisplay, '', sThumb, sDesc, oOutputParameterHandler)
                    listeUrlEpisode=[]
                    listeStitle=[]
  
            listeUrlEpisode.append(str(aEntry[1]) )
            sTitleEp =  sTitle +' '+ ' Saison ' + str(iSaison ) + ' Episode ' + str(iEpisode)
            listeStitle.append(sTitleEp )
            sTitleDisplay=sTitle +' '+ 'Saison' + ' '+ str(iSaison )
            if sYear:
                sTitleDisplay= sTitleDisplay + ' (' + sYear + ' )' 
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sThumb', sThumb)
        oOutputParameterHandler.addParameter('sDesc', sDesc)
        oOutputParameterHandler.addParameter('listeUrlEpisode', listeUrlEpisode)
        oOutputParameterHandler.addParameter('listeStitle', listeStitle)
        oOutputParameterHandler.addParameter('sYear', sYear)
        oGui.addTV(SITE_IDENTIFIER, 'showListEpisodes', sTitleDisplay, '', sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showListEpisodes():
    #parent https://mystream.zone/tvshows   
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sDesc = oInputParameterHandler.getValue('sDesc')
    sYear= oInputParameterHandler.getValue('sYear')
    listeUrlEpisode = oInputParameterHandler.getValue('listeUrlEpisode')
    listeStitle = oInputParameterHandler.getValue('listeStitle')
    
    listeUrlEpisode2=[]
    listeStitle2=[]
    sPattern="'([^']*)'"
    oParser = cParser()
    
    aResult = oParser.parse(listeUrlEpisode, sPattern)
    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)
    if (aResult[0] == True):
        for aEntry in aResult[1]:
            listeUrlEpisode2.append(aEntry)
            
    aResult = oParser.parse(listeStitle, sPattern)
    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)
    if (aResult[0] == True):
        for aEntry in aResult[1]:
            listeStitle2.append(aEntry)              
    i=0
    for itemurl in listeUrlEpisode2 :
        sTitle=listeStitle2[i]
        i=i+1
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl',itemurl )
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oOutputParameterHandler.addParameter('sThumb', sThumb)
        oOutputParameterHandler.addParameter('sDesc', sDesc)
        oOutputParameterHandler.addParameter('sYear', sYear)
        oGui.addEpisode(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
    
    oGui.setEndOfDirectory()

def showEpisodes():
    #parents https://mystream.zone/saisons/    
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sDesc = oInputParameterHandler.getValue('sDesc')
    sYear= oInputParameterHandler.getValue('sYear')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    #  thumb '2 - 11'   url  
    sPattern = "class='imagen'.+?src='([^']*).*?class='numerando'>([^<]*).+?href='([^']*)"
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)
     
    if (aResult[0] == True):

        for aEntry in aResult[1]:
            
            iSaison = re.search('([0-9]+)', aEntry[1]).group(1)
            iEpisode= re.search('([0-9]+)$', aEntry[1]).group(1)
            sUrl=aEntry[2]
            sTitleDisplay=sMovieTitle+' '+ ' Saison ' + str(iSaison ) + ' Episode ' + str(iEpisode)
            if sYear:
                sTitleDisplay= sTitleDisplay + ' (' + sYear + ' )' 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitleDisplay)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oOutputParameterHandler.addParameter('sYear', sYear)
            oGui.addEpisode(SITE_IDENTIFIER, 'showHosters', sTitleDisplay , '', sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showHosters():
    #parents:all
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sDesc= oInputParameterHandler.getValue('sDesc')
    sYear= oInputParameterHandler.getValue('sYear')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sPattern = "data-type='([^']*).*?post='([^']*).*?nume='([^']*).*?title'>([^<]*)"
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        for aEntry in aResult[1]:
            datatype=aEntry[0]
            datapost=aEntry[1]
            datanum=aEntry[2]
            sUrl2='https://mystream.zone/wp-admin/admin-ajax.php'
            pdata = 'action=doo_player_ajax&post=' + datapost + '&nume=' + datanum + '&type=' + datatype
            if sYear :
                sdisplayTitle= sTitle+ ' (' + sYear + ' )'
            else :
                sdisplayTitle= sTitle
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('referer', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sYear', sYear)
            oOutputParameterHandler.addParameter('pdata',pdata )
            oGui.addLink(SITE_IDENTIFIER, 'Hosterslink', sdisplayTitle, sThumb, sDesc, oOutputParameterHandler)
 
    oGui.setEndOfDirectory()

def Hosterslink ():
    #parents:all
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    referer = oInputParameterHandler.getValue('referer')
    pdata=oInputParameterHandler.getValue('pdata')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sYear= oInputParameterHandler.getValue('sYear') 
    if sYear :
        sMovieTitle= sMovieTitle + ' (' + sYear + ' )'   
    
    oRequest = cRequestHandler(sUrl)
    oRequest.setRequestType(1)
    oRequest.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:70.0) Gecko/20100101 Firefox/70.0')
    oRequest.addHeaderEntry('Referer', referer)
    oRequest.addHeaderEntry('Accept', '*/*')
    oRequest.addHeaderEntry('Accept-Language', 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3')
    oRequest.addHeaderEntry('Content-Type', 'application/x-www-form-urlencoded')
    oRequest.addParametersLine(pdata)

    sHtmlContent = oRequest.request()
    sPattern = '(?:<iframe|<IFRAME).+?(?:src|SRC)=(?:\'|")(.+?)(?:\'|")'
    aResult = oParser.parse(sHtmlContent, sPattern)
    
    
    if (aResult[0] == True):
        for aEntry in aResult[1]:
            sHosterUrl = aEntry
            
            ifVSlog('sHosterUrl='+str(sHosterUrl)) 
            
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if (oHoster != False):
                oHoster.setDisplayName(sMovieTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()

def ifVSlog(log):
    if bVSlog:
        try:  # si no import VSlog from resources.lib.comaddon
            VSlog(str(log)) 
        except:
            pass

