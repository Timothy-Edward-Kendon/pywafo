# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.00
# By python version 2.6.2 (r262:71605, Apr 14 2009, 22:40:02) [MSC v.1500 32 bit (Intel)]
# From type library 'msppt.olb'
# On Tue Dec 15 09:45:19 2009
"""Microsoft PowerPoint 11.0 Object Library"""
makepy_version = '0.5.00'
python_version = 0x20602f0

import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID #@UnresolvedImport
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty #@UndefinedVariable
defaultNamedNotOptArg=pythoncom.Empty #@UndefinedVariable
defaultUnnamedArg=pythoncom.Empty #@UndefinedVariable

global_Missing = pythoncom.Missing #@UndefinedVariable
global_IID_IDispatch = pythoncom.IID_IDispatch #@UndefinedVariable
global_IID_IConnectionPointContainer = pythoncom.IID_IConnectionPointContainer #@UndefinedVariable
global_com_error = pythoncom.com_error #@UndefinedVariable
global_error = pythoncom.error #@UndefinedVariable

CLSID = IID('{91493440-5A91-11CF-8700-00AA0060263B}')
MajorVersion = 2
MinorVersion = 8
LibraryFlags = 8
LCID = 0x0

class constants:
	msoAnimAccumulateAlways       =2          # from enum MsoAnimAccumulate
	msoAnimAccumulateNone         =1          # from enum MsoAnimAccumulate
	msoAnimAdditiveAddBase        =1          # from enum MsoAnimAdditive
	msoAnimAdditiveAddSum         =2          # from enum MsoAnimAdditive
	msoAnimAfterEffectDim         =1          # from enum MsoAnimAfterEffect
	msoAnimAfterEffectHide        =2          # from enum MsoAnimAfterEffect
	msoAnimAfterEffectHideOnNextClick=3          # from enum MsoAnimAfterEffect
	msoAnimAfterEffectMixed       =-1         # from enum MsoAnimAfterEffect
	msoAnimAfterEffectNone        =0          # from enum MsoAnimAfterEffect
	msoAnimCommandTypeCall        =1          # from enum MsoAnimCommandType
	msoAnimCommandTypeEvent       =0          # from enum MsoAnimCommandType
	msoAnimCommandTypeVerb        =2          # from enum MsoAnimCommandType
	msoAnimDirectionAcross        =18         # from enum MsoAnimDirection
	msoAnimDirectionBottom        =11         # from enum MsoAnimDirection
	msoAnimDirectionBottomLeft    =15         # from enum MsoAnimDirection
	msoAnimDirectionBottomRight   =14         # from enum MsoAnimDirection
	msoAnimDirectionCenter        =28         # from enum MsoAnimDirection
	msoAnimDirectionClockwise     =21         # from enum MsoAnimDirection
	msoAnimDirectionCounterclockwise=22         # from enum MsoAnimDirection
	msoAnimDirectionCycleClockwise=43         # from enum MsoAnimDirection
	msoAnimDirectionCycleCounterclockwise=44         # from enum MsoAnimDirection
	msoAnimDirectionDown          =3          # from enum MsoAnimDirection
	msoAnimDirectionDownLeft      =9          # from enum MsoAnimDirection
	msoAnimDirectionDownRight     =8          # from enum MsoAnimDirection
	msoAnimDirectionFontAllCaps   =40         # from enum MsoAnimDirection
	msoAnimDirectionFontBold      =35         # from enum MsoAnimDirection
	msoAnimDirectionFontItalic    =36         # from enum MsoAnimDirection
	msoAnimDirectionFontShadow    =39         # from enum MsoAnimDirection
	msoAnimDirectionFontStrikethrough=38         # from enum MsoAnimDirection
	msoAnimDirectionFontUnderline =37         # from enum MsoAnimDirection
	msoAnimDirectionGradual       =42         # from enum MsoAnimDirection
	msoAnimDirectionHorizontal    =16         # from enum MsoAnimDirection
	msoAnimDirectionHorizontalIn  =23         # from enum MsoAnimDirection
	msoAnimDirectionHorizontalOut =24         # from enum MsoAnimDirection
	msoAnimDirectionIn            =19         # from enum MsoAnimDirection
	msoAnimDirectionInBottom      =31         # from enum MsoAnimDirection
	msoAnimDirectionInCenter      =30         # from enum MsoAnimDirection
	msoAnimDirectionInSlightly    =29         # from enum MsoAnimDirection
	msoAnimDirectionInstant       =41         # from enum MsoAnimDirection
	msoAnimDirectionLeft          =4          # from enum MsoAnimDirection
	msoAnimDirectionNone          =0          # from enum MsoAnimDirection
	msoAnimDirectionOrdinalMask   =5          # from enum MsoAnimDirection
	msoAnimDirectionOut           =20         # from enum MsoAnimDirection
	msoAnimDirectionOutBottom     =34         # from enum MsoAnimDirection
	msoAnimDirectionOutCenter     =33         # from enum MsoAnimDirection
	msoAnimDirectionOutSlightly   =32         # from enum MsoAnimDirection
	msoAnimDirectionRight         =2          # from enum MsoAnimDirection
	msoAnimDirectionSlightly      =27         # from enum MsoAnimDirection
	msoAnimDirectionTop           =10         # from enum MsoAnimDirection
	msoAnimDirectionTopLeft       =12         # from enum MsoAnimDirection
	msoAnimDirectionTopRight      =13         # from enum MsoAnimDirection
	msoAnimDirectionUp            =1          # from enum MsoAnimDirection
	msoAnimDirectionUpLeft        =6          # from enum MsoAnimDirection
	msoAnimDirectionUpRight       =7          # from enum MsoAnimDirection
	msoAnimDirectionVertical      =17         # from enum MsoAnimDirection
	msoAnimDirectionVerticalIn    =25         # from enum MsoAnimDirection
	msoAnimDirectionVerticalOut   =26         # from enum MsoAnimDirection
	msoAnimEffectAppear           =1          # from enum MsoAnimEffect
	msoAnimEffectArcUp            =47         # from enum MsoAnimEffect
	msoAnimEffectAscend           =39         # from enum MsoAnimEffect
	msoAnimEffectBlast            =64         # from enum MsoAnimEffect
	msoAnimEffectBlinds           =3          # from enum MsoAnimEffect
	msoAnimEffectBoldFlash        =63         # from enum MsoAnimEffect
	msoAnimEffectBoldReveal       =65         # from enum MsoAnimEffect
	msoAnimEffectBoomerang        =25         # from enum MsoAnimEffect
	msoAnimEffectBounce           =26         # from enum MsoAnimEffect
	msoAnimEffectBox              =4          # from enum MsoAnimEffect
	msoAnimEffectBrushOnColor     =66         # from enum MsoAnimEffect
	msoAnimEffectBrushOnUnderline =67         # from enum MsoAnimEffect
	msoAnimEffectCenterRevolve    =40         # from enum MsoAnimEffect
	msoAnimEffectChangeFillColor  =54         # from enum MsoAnimEffect
	msoAnimEffectChangeFont       =55         # from enum MsoAnimEffect
	msoAnimEffectChangeFontColor  =56         # from enum MsoAnimEffect
	msoAnimEffectChangeFontSize   =57         # from enum MsoAnimEffect
	msoAnimEffectChangeFontStyle  =58         # from enum MsoAnimEffect
	msoAnimEffectChangeLineColor  =60         # from enum MsoAnimEffect
	msoAnimEffectCheckerboard     =5          # from enum MsoAnimEffect
	msoAnimEffectCircle           =6          # from enum MsoAnimEffect
	msoAnimEffectColorBlend       =68         # from enum MsoAnimEffect
	msoAnimEffectColorReveal      =27         # from enum MsoAnimEffect
	msoAnimEffectColorWave        =69         # from enum MsoAnimEffect
	msoAnimEffectComplementaryColor=70         # from enum MsoAnimEffect
	msoAnimEffectComplementaryColor2=71         # from enum MsoAnimEffect
	msoAnimEffectContrastingColor =72         # from enum MsoAnimEffect
	msoAnimEffectCrawl            =7          # from enum MsoAnimEffect
	msoAnimEffectCredits          =28         # from enum MsoAnimEffect
	msoAnimEffectCustom           =0          # from enum MsoAnimEffect
	msoAnimEffectDarken           =73         # from enum MsoAnimEffect
	msoAnimEffectDesaturate       =74         # from enum MsoAnimEffect
	msoAnimEffectDescend          =42         # from enum MsoAnimEffect
	msoAnimEffectDiamond          =8          # from enum MsoAnimEffect
	msoAnimEffectDissolve         =9          # from enum MsoAnimEffect
	msoAnimEffectEaseIn           =29         # from enum MsoAnimEffect
	msoAnimEffectExpand           =50         # from enum MsoAnimEffect
	msoAnimEffectFade             =10         # from enum MsoAnimEffect
	msoAnimEffectFadedSwivel      =41         # from enum MsoAnimEffect
	msoAnimEffectFadedZoom        =48         # from enum MsoAnimEffect
	msoAnimEffectFlashBulb        =75         # from enum MsoAnimEffect
	msoAnimEffectFlashOnce        =11         # from enum MsoAnimEffect
	msoAnimEffectFlicker          =76         # from enum MsoAnimEffect
	msoAnimEffectFlip             =51         # from enum MsoAnimEffect
	msoAnimEffectFloat            =30         # from enum MsoAnimEffect
	msoAnimEffectFly              =2          # from enum MsoAnimEffect
	msoAnimEffectFold             =53         # from enum MsoAnimEffect
	msoAnimEffectGlide            =49         # from enum MsoAnimEffect
	msoAnimEffectGrowAndTurn      =31         # from enum MsoAnimEffect
	msoAnimEffectGrowShrink       =59         # from enum MsoAnimEffect
	msoAnimEffectGrowWithColor    =77         # from enum MsoAnimEffect
	msoAnimEffectLightSpeed       =32         # from enum MsoAnimEffect
	msoAnimEffectLighten          =78         # from enum MsoAnimEffect
	msoAnimEffectMediaPause       =84         # from enum MsoAnimEffect
	msoAnimEffectMediaPlay        =83         # from enum MsoAnimEffect
	msoAnimEffectMediaStop        =85         # from enum MsoAnimEffect
	msoAnimEffectPath4PointStar   =101        # from enum MsoAnimEffect
	msoAnimEffectPath5PointStar   =90         # from enum MsoAnimEffect
	msoAnimEffectPath6PointStar   =96         # from enum MsoAnimEffect
	msoAnimEffectPath8PointStar   =102        # from enum MsoAnimEffect
	msoAnimEffectPathArcDown      =122        # from enum MsoAnimEffect
	msoAnimEffectPathArcLeft      =136        # from enum MsoAnimEffect
	msoAnimEffectPathArcRight     =143        # from enum MsoAnimEffect
	msoAnimEffectPathArcUp        =129        # from enum MsoAnimEffect
	msoAnimEffectPathBean         =116        # from enum MsoAnimEffect
	msoAnimEffectPathBounceLeft   =126        # from enum MsoAnimEffect
	msoAnimEffectPathBounceRight  =139        # from enum MsoAnimEffect
	msoAnimEffectPathBuzzsaw      =110        # from enum MsoAnimEffect
	msoAnimEffectPathCircle       =86         # from enum MsoAnimEffect
	msoAnimEffectPathCrescentMoon =91         # from enum MsoAnimEffect
	msoAnimEffectPathCurvedSquare =105        # from enum MsoAnimEffect
	msoAnimEffectPathCurvedX      =106        # from enum MsoAnimEffect
	msoAnimEffectPathCurvyLeft    =133        # from enum MsoAnimEffect
	msoAnimEffectPathCurvyRight   =146        # from enum MsoAnimEffect
	msoAnimEffectPathCurvyStar    =108        # from enum MsoAnimEffect
	msoAnimEffectPathDecayingWave =145        # from enum MsoAnimEffect
	msoAnimEffectPathDiagonalDownRight=134        # from enum MsoAnimEffect
	msoAnimEffectPathDiagonalUpRight=141        # from enum MsoAnimEffect
	msoAnimEffectPathDiamond      =88         # from enum MsoAnimEffect
	msoAnimEffectPathDown         =127        # from enum MsoAnimEffect
	msoAnimEffectPathEqualTriangle=98         # from enum MsoAnimEffect
	msoAnimEffectPathFigure8Four  =113        # from enum MsoAnimEffect
	msoAnimEffectPathFootball     =97         # from enum MsoAnimEffect
	msoAnimEffectPathFunnel       =137        # from enum MsoAnimEffect
	msoAnimEffectPathHeart        =94         # from enum MsoAnimEffect
	msoAnimEffectPathHeartbeat    =130        # from enum MsoAnimEffect
	msoAnimEffectPathHexagon      =89         # from enum MsoAnimEffect
	msoAnimEffectPathHorizontalFigure8=111        # from enum MsoAnimEffect
	msoAnimEffectPathInvertedSquare=119        # from enum MsoAnimEffect
	msoAnimEffectPathInvertedTriangle=118        # from enum MsoAnimEffect
	msoAnimEffectPathLeft         =120        # from enum MsoAnimEffect
	msoAnimEffectPathLoopdeLoop   =109        # from enum MsoAnimEffect
	msoAnimEffectPathNeutron      =114        # from enum MsoAnimEffect
	msoAnimEffectPathOctagon      =95         # from enum MsoAnimEffect
	msoAnimEffectPathParallelogram=99         # from enum MsoAnimEffect
	msoAnimEffectPathPeanut       =112        # from enum MsoAnimEffect
	msoAnimEffectPathPentagon     =100        # from enum MsoAnimEffect
	msoAnimEffectPathPlus         =117        # from enum MsoAnimEffect
	msoAnimEffectPathPointyStar   =104        # from enum MsoAnimEffect
	msoAnimEffectPathRight        =149        # from enum MsoAnimEffect
	msoAnimEffectPathRightTriangle=87         # from enum MsoAnimEffect
	msoAnimEffectPathSCurve1      =144        # from enum MsoAnimEffect
	msoAnimEffectPathSCurve2      =124        # from enum MsoAnimEffect
	msoAnimEffectPathSineWave     =125        # from enum MsoAnimEffect
	msoAnimEffectPathSpiralLeft   =140        # from enum MsoAnimEffect
	msoAnimEffectPathSpiralRight  =131        # from enum MsoAnimEffect
	msoAnimEffectPathSpring       =138        # from enum MsoAnimEffect
	msoAnimEffectPathSquare       =92         # from enum MsoAnimEffect
	msoAnimEffectPathStairsDown   =147        # from enum MsoAnimEffect
	msoAnimEffectPathSwoosh       =115        # from enum MsoAnimEffect
	msoAnimEffectPathTeardrop     =103        # from enum MsoAnimEffect
	msoAnimEffectPathTrapezoid    =93         # from enum MsoAnimEffect
	msoAnimEffectPathTurnDown     =135        # from enum MsoAnimEffect
	msoAnimEffectPathTurnRight    =121        # from enum MsoAnimEffect
	msoAnimEffectPathTurnUp       =128        # from enum MsoAnimEffect
	msoAnimEffectPathTurnUpRight  =142        # from enum MsoAnimEffect
	msoAnimEffectPathUp           =148        # from enum MsoAnimEffect
	msoAnimEffectPathVerticalFigure8=107        # from enum MsoAnimEffect
	msoAnimEffectPathWave         =132        # from enum MsoAnimEffect
	msoAnimEffectPathZigzag       =123        # from enum MsoAnimEffect
	msoAnimEffectPeek             =12         # from enum MsoAnimEffect
	msoAnimEffectPinwheel         =33         # from enum MsoAnimEffect
	msoAnimEffectPlus             =13         # from enum MsoAnimEffect
	msoAnimEffectRandomBars       =14         # from enum MsoAnimEffect
	msoAnimEffectRandomEffects    =24         # from enum MsoAnimEffect
	msoAnimEffectRiseUp           =34         # from enum MsoAnimEffect
	msoAnimEffectShimmer          =52         # from enum MsoAnimEffect
	msoAnimEffectSling            =43         # from enum MsoAnimEffect
	msoAnimEffectSpin             =61         # from enum MsoAnimEffect
	msoAnimEffectSpinner          =44         # from enum MsoAnimEffect
	msoAnimEffectSpiral           =15         # from enum MsoAnimEffect
	msoAnimEffectSplit            =16         # from enum MsoAnimEffect
	msoAnimEffectStretch          =17         # from enum MsoAnimEffect
	msoAnimEffectStretchy         =45         # from enum MsoAnimEffect
	msoAnimEffectStrips           =18         # from enum MsoAnimEffect
	msoAnimEffectStyleEmphasis    =79         # from enum MsoAnimEffect
	msoAnimEffectSwish            =35         # from enum MsoAnimEffect
	msoAnimEffectSwivel           =19         # from enum MsoAnimEffect
	msoAnimEffectTeeter           =80         # from enum MsoAnimEffect
	msoAnimEffectThinLine         =36         # from enum MsoAnimEffect
	msoAnimEffectTransparency     =62         # from enum MsoAnimEffect
	msoAnimEffectUnfold           =37         # from enum MsoAnimEffect
	msoAnimEffectVerticalGrow     =81         # from enum MsoAnimEffect
	msoAnimEffectWave             =82         # from enum MsoAnimEffect
	msoAnimEffectWedge            =20         # from enum MsoAnimEffect
	msoAnimEffectWheel            =21         # from enum MsoAnimEffect
	msoAnimEffectWhip             =38         # from enum MsoAnimEffect
	msoAnimEffectWipe             =22         # from enum MsoAnimEffect
	msoAnimEffectZip              =46         # from enum MsoAnimEffect
	msoAnimEffectZoom             =23         # from enum MsoAnimEffect
	msoAnimEffectAfterFreeze      =1          # from enum MsoAnimEffectAfter
	msoAnimEffectAfterHold        =3          # from enum MsoAnimEffectAfter
	msoAnimEffectAfterRemove      =2          # from enum MsoAnimEffectAfter
	msoAnimEffectAfterTransition  =4          # from enum MsoAnimEffectAfter
	msoAnimEffectRestartAlways    =1          # from enum MsoAnimEffectRestart
	msoAnimEffectRestartNever     =3          # from enum MsoAnimEffectRestart
	msoAnimEffectRestartWhenOff   =2          # from enum MsoAnimEffectRestart
	msoAnimFilterEffectSubtypeAcross=9          # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeDown=25         # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeDownLeft=14         # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeDownRight=16         # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeFromBottom=13         # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeFromLeft=10         # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeFromRight=11         # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeFromTop=12         # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeHorizontal=5          # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeIn  =7          # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeInHorizontal=3          # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeInVertical=1          # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeLeft=23         # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeNone=0          # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeOut =8          # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeOutHorizontal=4          # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeOutVertical=2          # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeRight=24         # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeSpokes1=18         # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeSpokes2=19         # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeSpokes3=20         # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeSpokes4=21         # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeSpokes8=22         # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeUp  =26         # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeUpLeft=15         # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeUpRight=17         # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectSubtypeVertical=6          # from enum MsoAnimFilterEffectSubtype
	msoAnimFilterEffectTypeBarn   =1          # from enum MsoAnimFilterEffectType
	msoAnimFilterEffectTypeBlinds =2          # from enum MsoAnimFilterEffectType
	msoAnimFilterEffectTypeBox    =3          # from enum MsoAnimFilterEffectType
	msoAnimFilterEffectTypeCheckerboard=4          # from enum MsoAnimFilterEffectType
	msoAnimFilterEffectTypeCircle =5          # from enum MsoAnimFilterEffectType
	msoAnimFilterEffectTypeDiamond=6          # from enum MsoAnimFilterEffectType
	msoAnimFilterEffectTypeDissolve=7          # from enum MsoAnimFilterEffectType
	msoAnimFilterEffectTypeFade   =8          # from enum MsoAnimFilterEffectType
	msoAnimFilterEffectTypeImage  =9          # from enum MsoAnimFilterEffectType
	msoAnimFilterEffectTypeNone   =0          # from enum MsoAnimFilterEffectType
	msoAnimFilterEffectTypePixelate=10         # from enum MsoAnimFilterEffectType
	msoAnimFilterEffectTypePlus   =11         # from enum MsoAnimFilterEffectType
	msoAnimFilterEffectTypeRandomBar=12         # from enum MsoAnimFilterEffectType
	msoAnimFilterEffectTypeSlide  =13         # from enum MsoAnimFilterEffectType
	msoAnimFilterEffectTypeStretch=14         # from enum MsoAnimFilterEffectType
	msoAnimFilterEffectTypeStrips =15         # from enum MsoAnimFilterEffectType
	msoAnimFilterEffectTypeWedge  =16         # from enum MsoAnimFilterEffectType
	msoAnimFilterEffectTypeWheel  =17         # from enum MsoAnimFilterEffectType
	msoAnimFilterEffectTypeWipe   =18         # from enum MsoAnimFilterEffectType
	msoAnimColor                  =7          # from enum MsoAnimProperty
	msoAnimHeight                 =4          # from enum MsoAnimProperty
	msoAnimNone                   =0          # from enum MsoAnimProperty
	msoAnimOpacity                =5          # from enum MsoAnimProperty
	msoAnimRotation               =6          # from enum MsoAnimProperty
	msoAnimShapeFillBackColor     =1007       # from enum MsoAnimProperty
	msoAnimShapeFillColor         =1005       # from enum MsoAnimProperty
	msoAnimShapeFillOn            =1004       # from enum MsoAnimProperty
	msoAnimShapeFillOpacity       =1006       # from enum MsoAnimProperty
	msoAnimShapeLineColor         =1009       # from enum MsoAnimProperty
	msoAnimShapeLineOn            =1008       # from enum MsoAnimProperty
	msoAnimShapePictureBrightness =1001       # from enum MsoAnimProperty
	msoAnimShapePictureContrast   =1000       # from enum MsoAnimProperty
	msoAnimShapePictureGamma      =1002       # from enum MsoAnimProperty
	msoAnimShapePictureGrayscale  =1003       # from enum MsoAnimProperty
	msoAnimShapeShadowColor       =1012       # from enum MsoAnimProperty
	msoAnimShapeShadowOffsetX     =1014       # from enum MsoAnimProperty
	msoAnimShapeShadowOffsetY     =1015       # from enum MsoAnimProperty
	msoAnimShapeShadowOn          =1010       # from enum MsoAnimProperty
	msoAnimShapeShadowOpacity     =1013       # from enum MsoAnimProperty
	msoAnimShapeShadowType        =1011       # from enum MsoAnimProperty
	msoAnimTextBulletCharacter    =111        # from enum MsoAnimProperty
	msoAnimTextBulletColor        =114        # from enum MsoAnimProperty
	msoAnimTextBulletFontName     =112        # from enum MsoAnimProperty
	msoAnimTextBulletNumber       =113        # from enum MsoAnimProperty
	msoAnimTextBulletRelativeSize =115        # from enum MsoAnimProperty
	msoAnimTextBulletStyle        =116        # from enum MsoAnimProperty
	msoAnimTextBulletType         =117        # from enum MsoAnimProperty
	msoAnimTextFontBold           =100        # from enum MsoAnimProperty
	msoAnimTextFontColor          =101        # from enum MsoAnimProperty
	msoAnimTextFontEmboss         =102        # from enum MsoAnimProperty
	msoAnimTextFontItalic         =103        # from enum MsoAnimProperty
	msoAnimTextFontName           =104        # from enum MsoAnimProperty
	msoAnimTextFontShadow         =105        # from enum MsoAnimProperty
	msoAnimTextFontSize           =106        # from enum MsoAnimProperty
	msoAnimTextFontStrikeThrough  =110        # from enum MsoAnimProperty
	msoAnimTextFontSubscript      =107        # from enum MsoAnimProperty
	msoAnimTextFontSuperscript    =108        # from enum MsoAnimProperty
	msoAnimTextFontUnderline      =109        # from enum MsoAnimProperty
	msoAnimVisibility             =8          # from enum MsoAnimProperty
	msoAnimWidth                  =3          # from enum MsoAnimProperty
	msoAnimX                      =1          # from enum MsoAnimProperty
	msoAnimY                      =2          # from enum MsoAnimProperty
	msoAnimTextUnitEffectByCharacter=1          # from enum MsoAnimTextUnitEffect
	msoAnimTextUnitEffectByParagraph=0          # from enum MsoAnimTextUnitEffect
	msoAnimTextUnitEffectByWord   =2          # from enum MsoAnimTextUnitEffect
	msoAnimTextUnitEffectMixed    =-1         # from enum MsoAnimTextUnitEffect
	msoAnimTriggerAfterPrevious   =3          # from enum MsoAnimTriggerType
	msoAnimTriggerMixed           =-1         # from enum MsoAnimTriggerType
	msoAnimTriggerNone            =0          # from enum MsoAnimTriggerType
	msoAnimTriggerOnPageClick     =1          # from enum MsoAnimTriggerType
	msoAnimTriggerOnShapeClick    =4          # from enum MsoAnimTriggerType
	msoAnimTriggerWithPrevious    =2          # from enum MsoAnimTriggerType
	msoAnimTypeColor              =2          # from enum MsoAnimType
	msoAnimTypeCommand            =6          # from enum MsoAnimType
	msoAnimTypeFilter             =7          # from enum MsoAnimType
	msoAnimTypeMixed              =-2         # from enum MsoAnimType
	msoAnimTypeMotion             =1          # from enum MsoAnimType
	msoAnimTypeNone               =0          # from enum MsoAnimType
	msoAnimTypeProperty           =5          # from enum MsoAnimType
	msoAnimTypeRotation           =4          # from enum MsoAnimType
	msoAnimTypeScale              =3          # from enum MsoAnimType
	msoAnimTypeSet                =8          # from enum MsoAnimType
	msoAnimateChartAllAtOnce      =7          # from enum MsoAnimateByLevel
	msoAnimateChartByCategory     =8          # from enum MsoAnimateByLevel
	msoAnimateChartByCategoryElements=9          # from enum MsoAnimateByLevel
	msoAnimateChartBySeries       =10         # from enum MsoAnimateByLevel
	msoAnimateChartBySeriesElements=11         # from enum MsoAnimateByLevel
	msoAnimateDiagramAllAtOnce    =12         # from enum MsoAnimateByLevel
	msoAnimateDiagramBreadthByLevel=16         # from enum MsoAnimateByLevel
	msoAnimateDiagramBreadthByNode=15         # from enum MsoAnimateByLevel
	msoAnimateDiagramClockwise    =17         # from enum MsoAnimateByLevel
	msoAnimateDiagramClockwiseIn  =18         # from enum MsoAnimateByLevel
	msoAnimateDiagramClockwiseOut =19         # from enum MsoAnimateByLevel
	msoAnimateDiagramCounterClockwise=20         # from enum MsoAnimateByLevel
	msoAnimateDiagramCounterClockwiseIn=21         # from enum MsoAnimateByLevel
	msoAnimateDiagramCounterClockwiseOut=22         # from enum MsoAnimateByLevel
	msoAnimateDiagramDepthByBranch=14         # from enum MsoAnimateByLevel
	msoAnimateDiagramDepthByNode  =13         # from enum MsoAnimateByLevel
	msoAnimateDiagramDown         =26         # from enum MsoAnimateByLevel
	msoAnimateDiagramInByRing     =23         # from enum MsoAnimateByLevel
	msoAnimateDiagramOutByRing    =24         # from enum MsoAnimateByLevel
	msoAnimateDiagramUp           =25         # from enum MsoAnimateByLevel
	msoAnimateLevelMixed          =-1         # from enum MsoAnimateByLevel
	msoAnimateLevelNone           =0          # from enum MsoAnimateByLevel
	msoAnimateTextByAllLevels     =1          # from enum MsoAnimateByLevel
	msoAnimateTextByFifthLevel    =6          # from enum MsoAnimateByLevel
	msoAnimateTextByFirstLevel    =2          # from enum MsoAnimateByLevel
	msoAnimateTextByFourthLevel   =5          # from enum MsoAnimateByLevel
	msoAnimateTextBySecondLevel   =3          # from enum MsoAnimateByLevel
	msoAnimateTextByThirdLevel    =4          # from enum MsoAnimateByLevel
	ppActionEndShow               =6          # from enum PpActionType
	ppActionFirstSlide            =3          # from enum PpActionType
	ppActionHyperlink             =7          # from enum PpActionType
	ppActionLastSlide             =4          # from enum PpActionType
	ppActionLastSlideViewed       =5          # from enum PpActionType
	ppActionMixed                 =-2         # from enum PpActionType
	ppActionNamedSlideShow        =10         # from enum PpActionType
	ppActionNextSlide             =1          # from enum PpActionType
	ppActionNone                  =0          # from enum PpActionType
	ppActionOLEVerb               =11         # from enum PpActionType
	ppActionPlay                  =12         # from enum PpActionType
	ppActionPreviousSlide         =2          # from enum PpActionType
	ppActionRunMacro              =8          # from enum PpActionType
	ppActionRunProgram            =9          # from enum PpActionType
	ppAdvanceModeMixed            =-2         # from enum PpAdvanceMode
	ppAdvanceOnClick              =1          # from enum PpAdvanceMode
	ppAdvanceOnTime               =2          # from enum PpAdvanceMode
	ppAfterEffectDim              =2          # from enum PpAfterEffect
	ppAfterEffectHide             =1          # from enum PpAfterEffect
	ppAfterEffectHideOnClick      =3          # from enum PpAfterEffect
	ppAfterEffectMixed            =-2         # from enum PpAfterEffect
	ppAfterEffectNothing          =0          # from enum PpAfterEffect
	ppAlertsAll                   =2          # from enum PpAlertLevel
	ppAlertsNone                  =1          # from enum PpAlertLevel
	ppArrangeCascade              =2          # from enum PpArrangeStyle
	ppArrangeTiled                =1          # from enum PpArrangeStyle
	ppAutoSizeMixed               =-2         # from enum PpAutoSize
	ppAutoSizeNone                =0          # from enum PpAutoSize
	ppAutoSizeShapeToFitText      =1          # from enum PpAutoSize
	ppBaselineAlignBaseline       =1          # from enum PpBaselineAlignment
	ppBaselineAlignCenter         =3          # from enum PpBaselineAlignment
	ppBaselineAlignFarEast50      =4          # from enum PpBaselineAlignment
	ppBaselineAlignMixed          =-2         # from enum PpBaselineAlignment
	ppBaselineAlignTop            =2          # from enum PpBaselineAlignment
	ppBorderBottom                =3          # from enum PpBorderType
	ppBorderDiagonalDown          =5          # from enum PpBorderType
	ppBorderDiagonalUp            =6          # from enum PpBorderType
	ppBorderLeft                  =2          # from enum PpBorderType
	ppBorderRight                 =4          # from enum PpBorderType
	ppBorderTop                   =1          # from enum PpBorderType
	ppBulletMixed                 =-2         # from enum PpBulletType
	ppBulletNone                  =0          # from enum PpBulletType
	ppBulletNumbered              =2          # from enum PpBulletType
	ppBulletPicture               =3          # from enum PpBulletType
	ppBulletUnnumbered            =1          # from enum PpBulletType
	ppCaseLower                   =2          # from enum PpChangeCase
	ppCaseSentence                =1          # from enum PpChangeCase
	ppCaseTitle                   =4          # from enum PpChangeCase
	ppCaseToggle                  =5          # from enum PpChangeCase
	ppCaseUpper                   =3          # from enum PpChangeCase
	ppAnimateByCategory           =2          # from enum PpChartUnitEffect
	ppAnimateByCategoryElements   =4          # from enum PpChartUnitEffect
	ppAnimateBySeries             =1          # from enum PpChartUnitEffect
	ppAnimateBySeriesElements     =3          # from enum PpChartUnitEffect
	ppAnimateChartAllAtOnce       =5          # from enum PpChartUnitEffect
	ppAnimateChartMixed           =-2         # from enum PpChartUnitEffect
	ppAccent1                     =6          # from enum PpColorSchemeIndex
	ppAccent2                     =7          # from enum PpColorSchemeIndex
	ppAccent3                     =8          # from enum PpColorSchemeIndex
	ppBackground                  =1          # from enum PpColorSchemeIndex
	ppFill                        =5          # from enum PpColorSchemeIndex
	ppForeground                  =2          # from enum PpColorSchemeIndex
	ppNotSchemeColor              =0          # from enum PpColorSchemeIndex
	ppSchemeColorMixed            =-2         # from enum PpColorSchemeIndex
	ppShadow                      =3          # from enum PpColorSchemeIndex
	ppTitle                       =4          # from enum PpColorSchemeIndex
	ppDateTimeFigureOut           =14         # from enum PpDateTimeFormat
	ppDateTimeFormatMixed         =-2         # from enum PpDateTimeFormat
	ppDateTimeHmm                 =10         # from enum PpDateTimeFormat
	ppDateTimeHmmss               =11         # from enum PpDateTimeFormat
	ppDateTimeMMMMdyyyy           =4          # from enum PpDateTimeFormat
	ppDateTimeMMMMyy              =6          # from enum PpDateTimeFormat
	ppDateTimeMMddyyHmm           =8          # from enum PpDateTimeFormat
	ppDateTimeMMddyyhmmAMPM       =9          # from enum PpDateTimeFormat
	ppDateTimeMMyy                =7          # from enum PpDateTimeFormat
	ppDateTimeMdyy                =1          # from enum PpDateTimeFormat
	ppDateTimedMMMMyyyy           =3          # from enum PpDateTimeFormat
	ppDateTimedMMMyy              =5          # from enum PpDateTimeFormat
	ppDateTimeddddMMMMddyyyy      =2          # from enum PpDateTimeFormat
	ppDateTimehmmAMPM             =12         # from enum PpDateTimeFormat
	ppDateTimehmmssAMPM           =13         # from enum PpDateTimeFormat
	ppDirectionLeftToRight        =1          # from enum PpDirection
	ppDirectionMixed              =-2         # from enum PpDirection
	ppDirectionRightToLeft        =2          # from enum PpDirection
	ppEffectAppear                =3844       # from enum PpEntryEffect
	ppEffectBlindsHorizontal      =769        # from enum PpEntryEffect
	ppEffectBlindsVertical        =770        # from enum PpEntryEffect
	ppEffectBoxIn                 =3074       # from enum PpEntryEffect
	ppEffectBoxOut                =3073       # from enum PpEntryEffect
	ppEffectCheckerboardAcross    =1025       # from enum PpEntryEffect
	ppEffectCheckerboardDown      =1026       # from enum PpEntryEffect
	ppEffectCircleOut             =3845       # from enum PpEntryEffect
	ppEffectCombHorizontal        =3847       # from enum PpEntryEffect
	ppEffectCombVertical          =3848       # from enum PpEntryEffect
	ppEffectCoverDown             =1284       # from enum PpEntryEffect
	ppEffectCoverLeft             =1281       # from enum PpEntryEffect
	ppEffectCoverLeftDown         =1287       # from enum PpEntryEffect
	ppEffectCoverLeftUp           =1285       # from enum PpEntryEffect
	ppEffectCoverRight            =1283       # from enum PpEntryEffect
	ppEffectCoverRightDown        =1288       # from enum PpEntryEffect
	ppEffectCoverRightUp          =1286       # from enum PpEntryEffect
	ppEffectCoverUp               =1282       # from enum PpEntryEffect
	ppEffectCrawlFromDown         =3344       # from enum PpEntryEffect
	ppEffectCrawlFromLeft         =3341       # from enum PpEntryEffect
	ppEffectCrawlFromRight        =3343       # from enum PpEntryEffect
	ppEffectCrawlFromUp           =3342       # from enum PpEntryEffect
	ppEffectCut                   =257        # from enum PpEntryEffect
	ppEffectCutThroughBlack       =258        # from enum PpEntryEffect
	ppEffectDiamondOut            =3846       # from enum PpEntryEffect
	ppEffectDissolve              =1537       # from enum PpEntryEffect
	ppEffectFade                  =1793       # from enum PpEntryEffect
	ppEffectFadeSmoothly          =3849       # from enum PpEntryEffect
	ppEffectFlashOnceFast         =3841       # from enum PpEntryEffect
	ppEffectFlashOnceMedium       =3842       # from enum PpEntryEffect
	ppEffectFlashOnceSlow         =3843       # from enum PpEntryEffect
	ppEffectFlyFromBottom         =3332       # from enum PpEntryEffect
	ppEffectFlyFromBottomLeft     =3335       # from enum PpEntryEffect
	ppEffectFlyFromBottomRight    =3336       # from enum PpEntryEffect
	ppEffectFlyFromLeft           =3329       # from enum PpEntryEffect
	ppEffectFlyFromRight          =3331       # from enum PpEntryEffect
	ppEffectFlyFromTop            =3330       # from enum PpEntryEffect
	ppEffectFlyFromTopLeft        =3333       # from enum PpEntryEffect
	ppEffectFlyFromTopRight       =3334       # from enum PpEntryEffect
	ppEffectMixed                 =-2         # from enum PpEntryEffect
	ppEffectNewsflash             =3850       # from enum PpEntryEffect
	ppEffectNone                  =0          # from enum PpEntryEffect
	ppEffectPeekFromDown          =3338       # from enum PpEntryEffect
	ppEffectPeekFromLeft          =3337       # from enum PpEntryEffect
	ppEffectPeekFromRight         =3339       # from enum PpEntryEffect
	ppEffectPeekFromUp            =3340       # from enum PpEntryEffect
	ppEffectPlusOut               =3851       # from enum PpEntryEffect
	ppEffectPushDown              =3852       # from enum PpEntryEffect
	ppEffectPushLeft              =3853       # from enum PpEntryEffect
	ppEffectPushRight             =3854       # from enum PpEntryEffect
	ppEffectPushUp                =3855       # from enum PpEntryEffect
	ppEffectRandom                =513        # from enum PpEntryEffect
	ppEffectRandomBarsHorizontal  =2305       # from enum PpEntryEffect
	ppEffectRandomBarsVertical    =2306       # from enum PpEntryEffect
	ppEffectSpiral                =3357       # from enum PpEntryEffect
	ppEffectSplitHorizontalIn     =3586       # from enum PpEntryEffect
	ppEffectSplitHorizontalOut    =3585       # from enum PpEntryEffect
	ppEffectSplitVerticalIn       =3588       # from enum PpEntryEffect
	ppEffectSplitVerticalOut      =3587       # from enum PpEntryEffect
	ppEffectStretchAcross         =3351       # from enum PpEntryEffect
	ppEffectStretchDown           =3355       # from enum PpEntryEffect
	ppEffectStretchLeft           =3352       # from enum PpEntryEffect
	ppEffectStretchRight          =3354       # from enum PpEntryEffect
	ppEffectStretchUp             =3353       # from enum PpEntryEffect
	ppEffectStripsDownLeft        =2563       # from enum PpEntryEffect
	ppEffectStripsDownRight       =2564       # from enum PpEntryEffect
	ppEffectStripsLeftDown        =2567       # from enum PpEntryEffect
	ppEffectStripsLeftUp          =2565       # from enum PpEntryEffect
	ppEffectStripsRightDown       =2568       # from enum PpEntryEffect
	ppEffectStripsRightUp         =2566       # from enum PpEntryEffect
	ppEffectStripsUpLeft          =2561       # from enum PpEntryEffect
	ppEffectStripsUpRight         =2562       # from enum PpEntryEffect
	ppEffectSwivel                =3356       # from enum PpEntryEffect
	ppEffectUncoverDown           =2052       # from enum PpEntryEffect
	ppEffectUncoverLeft           =2049       # from enum PpEntryEffect
	ppEffectUncoverLeftDown       =2055       # from enum PpEntryEffect
	ppEffectUncoverLeftUp         =2053       # from enum PpEntryEffect
	ppEffectUncoverRight          =2051       # from enum PpEntryEffect
	ppEffectUncoverRightDown      =2056       # from enum PpEntryEffect
	ppEffectUncoverRightUp        =2054       # from enum PpEntryEffect
	ppEffectUncoverUp             =2050       # from enum PpEntryEffect
	ppEffectWedge                 =3856       # from enum PpEntryEffect
	ppEffectWheel1Spoke           =3857       # from enum PpEntryEffect
	ppEffectWheel2Spokes          =3858       # from enum PpEntryEffect
	ppEffectWheel3Spokes          =3859       # from enum PpEntryEffect
	ppEffectWheel4Spokes          =3860       # from enum PpEntryEffect
	ppEffectWheel8Spokes          =3861       # from enum PpEntryEffect
	ppEffectWipeDown              =2820       # from enum PpEntryEffect
	ppEffectWipeLeft              =2817       # from enum PpEntryEffect
	ppEffectWipeRight             =2819       # from enum PpEntryEffect
	ppEffectWipeUp                =2818       # from enum PpEntryEffect
	ppEffectZoomBottom            =3350       # from enum PpEntryEffect
	ppEffectZoomCenter            =3349       # from enum PpEntryEffect
	ppEffectZoomIn                =3345       # from enum PpEntryEffect
	ppEffectZoomInSlightly        =3346       # from enum PpEntryEffect
	ppEffectZoomOut               =3347       # from enum PpEntryEffect
	ppEffectZoomOutSlightly       =3348       # from enum PpEntryEffect
	ppClipRelativeToSlide         =2          # from enum PpExportMode
	ppRelativeToSlide             =1          # from enum PpExportMode
	ppScaleToFit                  =3          # from enum PpExportMode
	ppScaleXY                     =4          # from enum PpExportMode
	ppFarEastLineBreakLevelCustom =3          # from enum PpFarEastLineBreakLevel
	ppFarEastLineBreakLevelNormal =1          # from enum PpFarEastLineBreakLevel
	ppFarEastLineBreakLevelStrict =2          # from enum PpFarEastLineBreakLevel
	ppFileDialogOpen              =1          # from enum PpFileDialogType
	ppFileDialogSave              =2          # from enum PpFileDialogType
	ppFollowColorsMixed           =-2         # from enum PpFollowColors
	ppFollowColorsNone            =0          # from enum PpFollowColors
	ppFollowColorsScheme          =1          # from enum PpFollowColors
	ppFollowColorsTextAndBackground=2          # from enum PpFollowColors
	ppFrameColorsBlackTextOnWhite =5          # from enum PpFrameColors
	ppFrameColorsBrowserColors    =1          # from enum PpFrameColors
	ppFrameColorsPresentationSchemeAccentColor=3          # from enum PpFrameColors
	ppFrameColorsPresentationSchemeTextColor=2          # from enum PpFrameColors
	ppFrameColorsWhiteTextOnBlack =4          # from enum PpFrameColors
	ppHTMLAutodetect              =4          # from enum PpHTMLVersion
	ppHTMLDual                    =3          # from enum PpHTMLVersion
	ppHTMLv3                      =1          # from enum PpHTMLVersion
	ppHTMLv4                      =2          # from enum PpHTMLVersion
	ppIndentControlMixed          =-2         # from enum PpIndentControl
	ppIndentKeepAttr              =2          # from enum PpIndentControl
	ppIndentReplaceAttr           =1          # from enum PpIndentControl
	ppMediaTypeMixed              =-2         # from enum PpMediaType
	ppMediaTypeMovie              =3          # from enum PpMediaType
	ppMediaTypeOther              =1          # from enum PpMediaType
	ppMediaTypeSound              =2          # from enum PpMediaType
	ppMouseClick                  =1          # from enum PpMouseActivation
	ppMouseOver                   =2          # from enum PpMouseActivation
	ppBulletAlphaLCParenBoth      =8          # from enum PpNumberedBulletStyle
	ppBulletAlphaLCParenRight     =9          # from enum PpNumberedBulletStyle
	ppBulletAlphaLCPeriod         =0          # from enum PpNumberedBulletStyle
	ppBulletAlphaUCParenBoth      =10         # from enum PpNumberedBulletStyle
	ppBulletAlphaUCParenRight     =11         # from enum PpNumberedBulletStyle
	ppBulletAlphaUCPeriod         =1          # from enum PpNumberedBulletStyle
	ppBulletArabicAbjadDash       =24         # from enum PpNumberedBulletStyle
	ppBulletArabicAlphaDash       =23         # from enum PpNumberedBulletStyle
	ppBulletArabicDBPeriod        =29         # from enum PpNumberedBulletStyle
	ppBulletArabicDBPlain         =28         # from enum PpNumberedBulletStyle
	ppBulletArabicParenBoth       =12         # from enum PpNumberedBulletStyle
	ppBulletArabicParenRight      =2          # from enum PpNumberedBulletStyle
	ppBulletArabicPeriod          =3          # from enum PpNumberedBulletStyle
	ppBulletArabicPlain           =13         # from enum PpNumberedBulletStyle
	ppBulletCircleNumDBPlain      =18         # from enum PpNumberedBulletStyle
	ppBulletCircleNumWDBlackPlain =20         # from enum PpNumberedBulletStyle
	ppBulletCircleNumWDWhitePlain =19         # from enum PpNumberedBulletStyle
	ppBulletHebrewAlphaDash       =25         # from enum PpNumberedBulletStyle
	ppBulletHindiAlpha1Period     =40         # from enum PpNumberedBulletStyle
	ppBulletHindiAlphaPeriod      =36         # from enum PpNumberedBulletStyle
	ppBulletHindiNumParenRight    =39         # from enum PpNumberedBulletStyle
	ppBulletHindiNumPeriod        =37         # from enum PpNumberedBulletStyle
	ppBulletKanjiKoreanPeriod     =27         # from enum PpNumberedBulletStyle
	ppBulletKanjiKoreanPlain      =26         # from enum PpNumberedBulletStyle
	ppBulletKanjiSimpChinDBPeriod =38         # from enum PpNumberedBulletStyle
	ppBulletRomanLCParenBoth      =4          # from enum PpNumberedBulletStyle
	ppBulletRomanLCParenRight     =5          # from enum PpNumberedBulletStyle
	ppBulletRomanLCPeriod         =6          # from enum PpNumberedBulletStyle
	ppBulletRomanUCParenBoth      =14         # from enum PpNumberedBulletStyle
	ppBulletRomanUCParenRight     =15         # from enum PpNumberedBulletStyle
	ppBulletRomanUCPeriod         =7          # from enum PpNumberedBulletStyle
	ppBulletSimpChinPeriod        =17         # from enum PpNumberedBulletStyle
	ppBulletSimpChinPlain         =16         # from enum PpNumberedBulletStyle
	ppBulletStyleMixed            =-2         # from enum PpNumberedBulletStyle
	ppBulletThaiAlphaParenBoth    =32         # from enum PpNumberedBulletStyle
	ppBulletThaiAlphaParenRight   =31         # from enum PpNumberedBulletStyle
	ppBulletThaiAlphaPeriod       =30         # from enum PpNumberedBulletStyle
	ppBulletThaiNumParenBoth      =35         # from enum PpNumberedBulletStyle
	ppBulletThaiNumParenRight     =34         # from enum PpNumberedBulletStyle
	ppBulletThaiNumPeriod         =33         # from enum PpNumberedBulletStyle
	ppBulletTradChinPeriod        =22         # from enum PpNumberedBulletStyle
	ppBulletTradChinPlain         =21         # from enum PpNumberedBulletStyle
	ppAlignCenter                 =2          # from enum PpParagraphAlignment
	ppAlignDistribute             =5          # from enum PpParagraphAlignment
	ppAlignJustify                =4          # from enum PpParagraphAlignment
	ppAlignJustifyLow             =7          # from enum PpParagraphAlignment
	ppAlignLeft                   =1          # from enum PpParagraphAlignment
	ppAlignRight                  =3          # from enum PpParagraphAlignment
	ppAlignThaiDistribute         =6          # from enum PpParagraphAlignment
	ppAlignmentMixed              =-2         # from enum PpParagraphAlignment
	ppPasteBitmap                 =1          # from enum PpPasteDataType
	ppPasteDefault                =0          # from enum PpPasteDataType
	ppPasteEnhancedMetafile       =2          # from enum PpPasteDataType
	ppPasteGIF                    =4          # from enum PpPasteDataType
	ppPasteHTML                   =8          # from enum PpPasteDataType
	ppPasteJPG                    =5          # from enum PpPasteDataType
	ppPasteMetafilePicture        =3          # from enum PpPasteDataType
	ppPasteOLEObject              =10         # from enum PpPasteDataType
	ppPastePNG                    =6          # from enum PpPasteDataType
	ppPasteRTF                    =9          # from enum PpPasteDataType
	ppPasteShape                  =11         # from enum PpPasteDataType
	ppPasteText                   =7          # from enum PpPasteDataType
	ppPlaceholderBitmap           =9          # from enum PpPlaceholderType
	ppPlaceholderBody             =2          # from enum PpPlaceholderType
	ppPlaceholderCenterTitle      =3          # from enum PpPlaceholderType
	ppPlaceholderChart            =8          # from enum PpPlaceholderType
	ppPlaceholderDate             =16         # from enum PpPlaceholderType
	ppPlaceholderFooter           =15         # from enum PpPlaceholderType
	ppPlaceholderHeader           =14         # from enum PpPlaceholderType
	ppPlaceholderMediaClip        =10         # from enum PpPlaceholderType
	ppPlaceholderMixed            =-2         # from enum PpPlaceholderType
	ppPlaceholderObject           =7          # from enum PpPlaceholderType
	ppPlaceholderOrgChart         =11         # from enum PpPlaceholderType
	ppPlaceholderSlideNumber      =13         # from enum PpPlaceholderType
	ppPlaceholderSubtitle         =4          # from enum PpPlaceholderType
	ppPlaceholderTable            =12         # from enum PpPlaceholderType
	ppPlaceholderTitle            =1          # from enum PpPlaceholderType
	ppPlaceholderVerticalBody     =6          # from enum PpPlaceholderType
	ppPlaceholderVerticalTitle    =5          # from enum PpPlaceholderType
	ppPrintBlackAndWhite          =2          # from enum PpPrintColorType
	ppPrintColor                  =1          # from enum PpPrintColorType
	ppPrintPureBlackAndWhite      =3          # from enum PpPrintColorType
	ppPrintHandoutHorizontalFirst =2          # from enum PpPrintHandoutOrder
	ppPrintHandoutVerticalFirst   =1          # from enum PpPrintHandoutOrder
	ppPrintOutputBuildSlides      =7          # from enum PpPrintOutputType
	ppPrintOutputFourSlideHandouts=8          # from enum PpPrintOutputType
	ppPrintOutputNineSlideHandouts=9          # from enum PpPrintOutputType
	ppPrintOutputNotesPages       =5          # from enum PpPrintOutputType
	ppPrintOutputOneSlideHandouts =10         # from enum PpPrintOutputType
	ppPrintOutputOutline          =6          # from enum PpPrintOutputType
	ppPrintOutputSixSlideHandouts =4          # from enum PpPrintOutputType
	ppPrintOutputSlides           =1          # from enum PpPrintOutputType
	ppPrintOutputThreeSlideHandouts=3          # from enum PpPrintOutputType
	ppPrintOutputTwoSlideHandouts =2          # from enum PpPrintOutputType
	ppPrintAll                    =1          # from enum PpPrintRangeType
	ppPrintCurrent                =3          # from enum PpPrintRangeType
	ppPrintNamedSlideShow         =5          # from enum PpPrintRangeType
	ppPrintSelection              =2          # from enum PpPrintRangeType
	ppPrintSlideRange             =4          # from enum PpPrintRangeType
	ppPublishAll                  =1          # from enum PpPublishSourceType
	ppPublishNamedSlideShow       =3          # from enum PpPublishSourceType
	ppPublishSlideRange           =2          # from enum PpPublishSourceType
	ppRevisionInfoBaseline        =1          # from enum PpRevisionInfo
	ppRevisionInfoMerged          =2          # from enum PpRevisionInfo
	ppRevisionInfoNone            =0          # from enum PpRevisionInfo
	ppSaveAsAddIn                 =8          # from enum PpSaveAsFileType
	ppSaveAsBMP                   =19         # from enum PpSaveAsFileType
	ppSaveAsDefault               =11         # from enum PpSaveAsFileType
	ppSaveAsEMF                   =23         # from enum PpSaveAsFileType
	ppSaveAsGIF                   =16         # from enum PpSaveAsFileType
	ppSaveAsHTML                  =12         # from enum PpSaveAsFileType
	ppSaveAsHTMLDual              =14         # from enum PpSaveAsFileType
	ppSaveAsHTMLv3                =13         # from enum PpSaveAsFileType
	ppSaveAsJPG                   =17         # from enum PpSaveAsFileType
	ppSaveAsMetaFile              =15         # from enum PpSaveAsFileType
	ppSaveAsPNG                   =18         # from enum PpSaveAsFileType
	ppSaveAsPowerPoint3           =4          # from enum PpSaveAsFileType
	ppSaveAsPowerPoint4           =3          # from enum PpSaveAsFileType
	ppSaveAsPowerPoint4FarEast    =10         # from enum PpSaveAsFileType
	ppSaveAsPowerPoint7           =2          # from enum PpSaveAsFileType
	ppSaveAsPresForReview         =22         # from enum PpSaveAsFileType
	ppSaveAsPresentation          =1          # from enum PpSaveAsFileType
	ppSaveAsRTF                   =6          # from enum PpSaveAsFileType
	ppSaveAsShow                  =7          # from enum PpSaveAsFileType
	ppSaveAsTIF                   =21         # from enum PpSaveAsFileType
	ppSaveAsTemplate              =5          # from enum PpSaveAsFileType
	ppSaveAsWebArchive            =20         # from enum PpSaveAsFileType
	ppSelectionNone               =0          # from enum PpSelectionType
	ppSelectionShapes             =2          # from enum PpSelectionType
	ppSelectionSlides             =1          # from enum PpSelectionType
	ppSelectionText               =3          # from enum PpSelectionType
	ppShapeFormatBMP              =3          # from enum PpShapeFormat
	ppShapeFormatEMF              =5          # from enum PpShapeFormat
	ppShapeFormatGIF              =0          # from enum PpShapeFormat
	ppShapeFormatJPG              =1          # from enum PpShapeFormat
	ppShapeFormatPNG              =2          # from enum PpShapeFormat
	ppShapeFormatWMF              =4          # from enum PpShapeFormat
	ppLayoutBlank                 =12         # from enum PpSlideLayout
	ppLayoutChart                 =8          # from enum PpSlideLayout
	ppLayoutChartAndText          =6          # from enum PpSlideLayout
	ppLayoutClipArtAndVerticalText=26         # from enum PpSlideLayout
	ppLayoutClipartAndText        =10         # from enum PpSlideLayout
	ppLayoutFourObjects           =24         # from enum PpSlideLayout
	ppLayoutLargeObject           =15         # from enum PpSlideLayout
	ppLayoutMediaClipAndText      =18         # from enum PpSlideLayout
	ppLayoutMixed                 =-2         # from enum PpSlideLayout
	ppLayoutObject                =16         # from enum PpSlideLayout
	ppLayoutObjectAndText         =14         # from enum PpSlideLayout
	ppLayoutObjectAndTwoObjects   =30         # from enum PpSlideLayout
	ppLayoutObjectOverText        =19         # from enum PpSlideLayout
	ppLayoutOrgchart              =7          # from enum PpSlideLayout
	ppLayoutTable                 =4          # from enum PpSlideLayout
	ppLayoutText                  =2          # from enum PpSlideLayout
	ppLayoutTextAndChart          =5          # from enum PpSlideLayout
	ppLayoutTextAndClipart        =9          # from enum PpSlideLayout
	ppLayoutTextAndMediaClip      =17         # from enum PpSlideLayout
	ppLayoutTextAndObject         =13         # from enum PpSlideLayout
	ppLayoutTextAndTwoObjects     =21         # from enum PpSlideLayout
	ppLayoutTextOverObject        =20         # from enum PpSlideLayout
	ppLayoutTitle                 =1          # from enum PpSlideLayout
	ppLayoutTitleOnly             =11         # from enum PpSlideLayout
	ppLayoutTwoColumnText         =3          # from enum PpSlideLayout
	ppLayoutTwoObjects            =29         # from enum PpSlideLayout
	ppLayoutTwoObjectsAndObject   =31         # from enum PpSlideLayout
	ppLayoutTwoObjectsAndText     =22         # from enum PpSlideLayout
	ppLayoutTwoObjectsOverText    =23         # from enum PpSlideLayout
	ppLayoutVerticalText          =25         # from enum PpSlideLayout
	ppLayoutVerticalTitleAndText  =27         # from enum PpSlideLayout
	ppLayoutVerticalTitleAndTextOverChart=28         # from enum PpSlideLayout
	ppSlideShowManualAdvance      =1          # from enum PpSlideShowAdvanceMode
	ppSlideShowRehearseNewTimings =3          # from enum PpSlideShowAdvanceMode
	ppSlideShowUseSlideTimings    =2          # from enum PpSlideShowAdvanceMode
	ppSlideShowPointerAlwaysHidden=3          # from enum PpSlideShowPointerType
	ppSlideShowPointerArrow       =1          # from enum PpSlideShowPointerType
	ppSlideShowPointerAutoArrow   =4          # from enum PpSlideShowPointerType
	ppSlideShowPointerEraser      =5          # from enum PpSlideShowPointerType
	ppSlideShowPointerNone        =0          # from enum PpSlideShowPointerType
	ppSlideShowPointerPen         =2          # from enum PpSlideShowPointerType
	ppShowAll                     =1          # from enum PpSlideShowRangeType
	ppShowNamedSlideShow          =3          # from enum PpSlideShowRangeType
	ppShowSlideRange              =2          # from enum PpSlideShowRangeType
	ppSlideShowBlackScreen        =3          # from enum PpSlideShowState
	ppSlideShowDone               =5          # from enum PpSlideShowState
	ppSlideShowPaused             =2          # from enum PpSlideShowState
	ppSlideShowRunning            =1          # from enum PpSlideShowState
	ppSlideShowWhiteScreen        =4          # from enum PpSlideShowState
	ppShowTypeKiosk               =3          # from enum PpSlideShowType
	ppShowTypeSpeaker             =1          # from enum PpSlideShowType
	ppShowTypeWindow              =2          # from enum PpSlideShowType
	ppSlideSize35MM               =4          # from enum PpSlideSizeType
	ppSlideSizeA3Paper            =9          # from enum PpSlideSizeType
	ppSlideSizeA4Paper            =3          # from enum PpSlideSizeType
	ppSlideSizeB4ISOPaper         =10         # from enum PpSlideSizeType
	ppSlideSizeB4JISPaper         =12         # from enum PpSlideSizeType
	ppSlideSizeB5ISOPaper         =11         # from enum PpSlideSizeType
	ppSlideSizeB5JISPaper         =13         # from enum PpSlideSizeType
	ppSlideSizeBanner             =6          # from enum PpSlideSizeType
	ppSlideSizeCustom             =7          # from enum PpSlideSizeType
	ppSlideSizeHagakiCard         =14         # from enum PpSlideSizeType
	ppSlideSizeLedgerPaper        =8          # from enum PpSlideSizeType
	ppSlideSizeLetterPaper        =2          # from enum PpSlideSizeType
	ppSlideSizeOnScreen           =1          # from enum PpSlideSizeType
	ppSlideSizeOverhead           =5          # from enum PpSlideSizeType
	ppSoundEffectsMixed           =-2         # from enum PpSoundEffectType
	ppSoundFile                   =2          # from enum PpSoundEffectType
	ppSoundNone                   =0          # from enum PpSoundEffectType
	ppSoundStopPrevious           =1          # from enum PpSoundEffectType
	ppSoundFormatCDAudio          =3          # from enum PpSoundFormatType
	ppSoundFormatMIDI             =2          # from enum PpSoundFormatType
	ppSoundFormatMixed            =-2         # from enum PpSoundFormatType
	ppSoundFormatNone             =0          # from enum PpSoundFormatType
	ppSoundFormatWAV              =1          # from enum PpSoundFormatType
	ppTabStopCenter               =2          # from enum PpTabStopType
	ppTabStopDecimal              =4          # from enum PpTabStopType
	ppTabStopLeft                 =1          # from enum PpTabStopType
	ppTabStopMixed                =-2         # from enum PpTabStopType
	ppTabStopRight                =3          # from enum PpTabStopType
	ppAnimateByAllLevels          =16         # from enum PpTextLevelEffect
	ppAnimateByFifthLevel         =5          # from enum PpTextLevelEffect
	ppAnimateByFirstLevel         =1          # from enum PpTextLevelEffect
	ppAnimateByFourthLevel        =4          # from enum PpTextLevelEffect
	ppAnimateBySecondLevel        =2          # from enum PpTextLevelEffect
	ppAnimateByThirdLevel         =3          # from enum PpTextLevelEffect
	ppAnimateLevelMixed           =-2         # from enum PpTextLevelEffect
	ppAnimateLevelNone            =0          # from enum PpTextLevelEffect
	ppBodyStyle                   =3          # from enum PpTextStyleType
	ppDefaultStyle                =1          # from enum PpTextStyleType
	ppTitleStyle                  =2          # from enum PpTextStyleType
	ppAnimateByCharacter          =2          # from enum PpTextUnitEffect
	ppAnimateByParagraph          =0          # from enum PpTextUnitEffect
	ppAnimateByWord               =1          # from enum PpTextUnitEffect
	ppAnimateUnitMixed            =-2         # from enum PpTextUnitEffect
	ppTransitionSpeedFast         =3          # from enum PpTransitionSpeed
	ppTransitionSpeedMedium       =2          # from enum PpTransitionSpeed
	ppTransitionSpeedMixed        =-2         # from enum PpTransitionSpeed
	ppTransitionSpeedSlow         =1          # from enum PpTransitionSpeed
	ppUpdateOptionAutomatic       =2          # from enum PpUpdateOption
	ppUpdateOptionManual          =1          # from enum PpUpdateOption
	ppUpdateOptionMixed           =-2         # from enum PpUpdateOption
	ppViewHandoutMaster           =4          # from enum PpViewType
	ppViewMasterThumbnails        =12         # from enum PpViewType
	ppViewNormal                  =9          # from enum PpViewType
	ppViewNotesMaster             =5          # from enum PpViewType
	ppViewNotesPage               =3          # from enum PpViewType
	ppViewOutline                 =6          # from enum PpViewType
	ppViewPrintPreview            =10         # from enum PpViewType
	ppViewSlide                   =1          # from enum PpViewType
	ppViewSlideMaster             =2          # from enum PpViewType
	ppViewSlideSorter             =7          # from enum PpViewType
	ppViewThumbnails              =11         # from enum PpViewType
	ppViewTitleMaster             =8          # from enum PpViewType
	ppWindowMaximized             =3          # from enum PpWindowState
	ppWindowMinimized             =2          # from enum PpWindowState
	ppWindowNormal                =1          # from enum PpWindowState

from win32com.client import DispatchBaseClass
class ActionSetting(DispatchBaseClass):
	CLSID = IID('{9149348D-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Action": (2003, 2, (3, 0), (), "Action", None),
		"ActionVerb": (2004, 2, (8, 0), (), "ActionVerb", None),
		"AnimateAction": (2005, 2, (3, 0), (), "AnimateAction", None),
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Hyperlink' returns object of type 'Hyperlink'
		"Hyperlink": (2008, 2, (9, 0), (), "Hyperlink", '{91493465-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Run": (2006, 2, (8, 0), (), "Run", None),
		"ShowAndReturn": (2010, 2, (3, 0), (), "ShowAndReturn", None),
		"SlideShowName": (2007, 2, (8, 0), (), "SlideShowName", None),
		# Method 'SoundEffect' returns object of type 'SoundEffect'
		"SoundEffect": (2009, 2, (9, 0), (), "SoundEffect", '{91493472-5A91-11CF-8700-00AA0060263B}'),
	}
	_prop_map_put_ = {
		"Action": ((2003, LCID, 4, 0),()),
		"ActionVerb": ((2004, LCID, 4, 0),()),
		"AnimateAction": ((2005, LCID, 4, 0),()),
		"Run": ((2006, LCID, 4, 0),()),
		"ShowAndReturn": ((2010, LCID, 4, 0),()),
		"SlideShowName": ((2007, LCID, 4, 0),()),
	}

class ActionSettings(DispatchBaseClass):
	CLSID = IID('{9149348C-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type ActionSetting
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{9149348D-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{9149348D-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{9149348D-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{9149348D-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class AddIn(DispatchBaseClass):
	CLSID = IID('{91493461-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"AutoLoad": (2007, 2, (3, 0), (), "AutoLoad", None),
		"DisplayAlerts": (2009, 2, (3, 0), (), "DisplayAlerts", None),
		"FullName": (2003, 2, (8, 0), (), "FullName", None),
		"Loaded": (2008, 2, (3, 0), (), "Loaded", None),
		"Name": (2004, 2, (8, 0), (), "Name", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Path": (2005, 2, (8, 0), (), "Path", None),
		"Registered": (2006, 2, (3, 0), (), "Registered", None),
		"RegisteredInHKLM": (2010, 2, (3, 0), (), "RegisteredInHKLM", None),
	}
	_prop_map_put_ = {
		"AutoLoad": ((2007, LCID, 4, 0),()),
		"DisplayAlerts": ((2009, LCID, 4, 0),()),
		"Loaded": ((2008, LCID, 4, 0),()),
		"Registered": ((2006, LCID, 4, 0),()),
	}

class AddIns(DispatchBaseClass):
	CLSID = IID('{91493460-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type AddIn
	def Add(self, FileName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(2003, LCID, 1, (9, 0), ((8, 1),),FileName
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{91493461-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type AddIn
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((16396, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{91493461-5A91-11CF-8700-00AA0060263B}')
		return ret

	def Remove(self, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2004, LCID, 1, (24, 0), ((16396, 1),),Index
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((16396, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{91493461-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{91493461-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{91493461-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class Adjustments(DispatchBaseClass):
	CLSID = IID('{9149347C-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(0, LCID, 2, (4, 0), ((3, 1),),Index
			)

	# The method SetItem is actually a property, but must be used as a method to correctly pass the arguments
	def SetItem(self, Index=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 4, (24, 0), ((3, 1), (4, 1)),Index
			, arg1)

	_prop_map_get_ = {
		"Application": (2001, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(0, LCID, 2, (4, 0), ((3, 1),),Index
			)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class AnimationBehavior(DispatchBaseClass):
	CLSID = IID('{914934E4-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Delete(self):
		return self._oleobj_.InvokeTypes(2012, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Accumulate": (2004, 2, (3, 0), (), "Accumulate", None),
		"Additive": (2003, 2, (3, 0), (), "Additive", None),
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		# Method 'ColorEffect' returns object of type 'ColorEffect'
		"ColorEffect": (2007, 2, (9, 0), (), "ColorEffect", '{914934E6-5A91-11CF-8700-00AA0060263B}'),
		# Method 'CommandEffect' returns object of type 'CommandEffect'
		"CommandEffect": (2013, 2, (9, 0), (), "CommandEffect", '{914934EF-5A91-11CF-8700-00AA0060263B}'),
		# Method 'FilterEffect' returns object of type 'FilterEffect'
		"FilterEffect": (2014, 2, (9, 0), (), "FilterEffect", '{914934F0-5A91-11CF-8700-00AA0060263B}'),
		# Method 'MotionEffect' returns object of type 'MotionEffect'
		"MotionEffect": (2006, 2, (9, 0), (), "MotionEffect", '{914934E5-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		# Method 'PropertyEffect' returns object of type 'PropertyEffect'
		"PropertyEffect": (2010, 2, (9, 0), (), "PropertyEffect", '{914934E9-5A91-11CF-8700-00AA0060263B}'),
		# Method 'RotationEffect' returns object of type 'RotationEffect'
		"RotationEffect": (2009, 2, (9, 0), (), "RotationEffect", '{914934E8-5A91-11CF-8700-00AA0060263B}'),
		# Method 'ScaleEffect' returns object of type 'ScaleEffect'
		"ScaleEffect": (2008, 2, (9, 0), (), "ScaleEffect", '{914934E7-5A91-11CF-8700-00AA0060263B}'),
		# Method 'SetEffect' returns object of type 'SetEffect'
		"SetEffect": (2015, 2, (9, 0), (), "SetEffect", '{914934F1-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Timing' returns object of type 'Timing'
		"Timing": (2011, 2, (9, 0), (), "Timing", '{914934E0-5A91-11CF-8700-00AA0060263B}'),
		"Type": (2005, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Accumulate": ((2004, LCID, 4, 0),()),
		"Additive": ((2003, LCID, 4, 0),()),
		"Type": ((2005, LCID, 4, 0),()),
	}

class AnimationBehaviors(DispatchBaseClass):
	CLSID = IID('{914934E3-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type AnimationBehavior
	def Add(self, Type=defaultNamedNotOptArg, Index=-1):
		ret = self._oleobj_.InvokeTypes(2003, LCID, 1, (9, 0), ((3, 1), (3, 49)),Type
			, Index)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{914934E4-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type AnimationBehavior
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{914934E4-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{914934E4-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{914934E4-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{914934E4-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class AnimationPoint(DispatchBaseClass):
	CLSID = IID('{914934EB-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Delete(self):
		return self._oleobj_.InvokeTypes(2003, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Formula": (2006, 2, (8, 0), (), "Formula", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Time": (2004, 2, (4, 0), (), "Time", None),
		"Value": (2005, 2, (12, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"Formula": ((2006, LCID, 4, 0),()),
		"Time": ((2004, LCID, 4, 0),()),
		"Value": ((2005, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(2005, 2, (12, 0), (), "Value", None))
	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class AnimationPoints(DispatchBaseClass):
	CLSID = IID('{914934EA-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type AnimationPoint
	def Add(self, Index=-1):
		ret = self._oleobj_.InvokeTypes(2003, LCID, 1, (9, 0), ((3, 49),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{914934EB-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type AnimationPoint
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{914934EB-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Smooth": (2004, 2, (3, 0), (), "Smooth", None),
	}
	_prop_map_put_ = {
		"Smooth": ((2004, LCID, 4, 0),()),
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{914934EB-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{914934EB-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{914934EB-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class AnimationSettings(DispatchBaseClass):
	CLSID = IID('{9149348B-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		"AdvanceMode": (2008, 2, (3, 0), (), "AdvanceMode", None),
		"AdvanceTime": (2009, 2, (4, 0), (), "AdvanceTime", None),
		"AfterEffect": (2006, 2, (3, 0), (), "AfterEffect", None),
		"Animate": (2013, 2, (3, 0), (), "Animate", None),
		"AnimateBackground": (2014, 2, (3, 0), (), "AnimateBackground", None),
		"AnimateTextInReverse": (2015, 2, (3, 0), (), "AnimateTextInReverse", None),
		"AnimationOrder": (2007, 2, (3, 0), (), "AnimationOrder", None),
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"ChartUnitEffect": (2016, 2, (3, 0), (), "ChartUnitEffect", None),
		# Method 'DimColor' returns object of type 'ColorFormat'
		"DimColor": (2003, 2, (9, 0), (), "DimColor", '{91493452-5A91-11CF-8700-00AA0060263B}'),
		"EntryEffect": (2005, 2, (3, 0), (), "EntryEffect", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		# Method 'PlaySettings' returns object of type 'PlaySettings'
		"PlaySettings": (2010, 2, (9, 0), (), "PlaySettings", '{9149348E-5A91-11CF-8700-00AA0060263B}'),
		# Method 'SoundEffect' returns object of type 'SoundEffect'
		"SoundEffect": (2004, 2, (9, 0), (), "SoundEffect", '{91493472-5A91-11CF-8700-00AA0060263B}'),
		"TextLevelEffect": (2011, 2, (3, 0), (), "TextLevelEffect", None),
		"TextUnitEffect": (2012, 2, (3, 0), (), "TextUnitEffect", None),
	}
	_prop_map_put_ = {
		"AdvanceMode": ((2008, LCID, 4, 0),()),
		"AdvanceTime": ((2009, LCID, 4, 0),()),
		"AfterEffect": ((2006, LCID, 4, 0),()),
		"Animate": ((2013, LCID, 4, 0),()),
		"AnimateBackground": ((2014, LCID, 4, 0),()),
		"AnimateTextInReverse": ((2015, LCID, 4, 0),()),
		"AnimationOrder": ((2007, LCID, 4, 0),()),
		"ChartUnitEffect": ((2016, LCID, 4, 0),()),
		"EntryEffect": ((2005, LCID, 4, 0),()),
		"TextLevelEffect": ((2011, LCID, 4, 0),()),
		"TextUnitEffect": ((2012, LCID, 4, 0),()),
	}

class AutoCorrect(DispatchBaseClass):
	CLSID = IID('{914934ED-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		"DisplayAutoCorrectOptions": (2001, 2, (11, 0), (), "DisplayAutoCorrectOptions", None),
		"DisplayAutoLayoutOptions": (2002, 2, (11, 0), (), "DisplayAutoLayoutOptions", None),
	}
	_prop_map_put_ = {
		"DisplayAutoCorrectOptions": ((2001, LCID, 4, 0),()),
		"DisplayAutoLayoutOptions": ((2002, LCID, 4, 0),()),
	}

class Borders(DispatchBaseClass):
	CLSID = IID('{914934CA-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type LineFormat
	def Item(self, BorderType=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),BorderType
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{9149347F-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, BorderType=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),BorderType
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{9149347F-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{9149347F-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{9149347F-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class BulletFormat(DispatchBaseClass):
	CLSID = IID('{91493497-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Picture(self, Picture=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2011, LCID, 1, (24, 0), ((8, 1),),Picture
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Character": (2003, 2, (3, 0), (), "Character", None),
		# Method 'Font' returns object of type 'Font'
		"Font": (2007, 2, (9, 0), (), "Font", '{91493495-5A91-11CF-8700-00AA0060263B}'),
		"Number": (2012, 2, (3, 0), (), "Number", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"RelativeSize": (2004, 2, (4, 0), (), "RelativeSize", None),
		"StartValue": (2010, 2, (3, 0), (), "StartValue", None),
		"Style": (2009, 2, (3, 0), (), "Style", None),
		"Type": (2008, 2, (3, 0), (), "Type", None),
		"UseTextColor": (2005, 2, (3, 0), (), "UseTextColor", None),
		"UseTextFont": (2006, 2, (3, 0), (), "UseTextFont", None),
		"Visible": (0, 2, (3, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Character": ((2003, LCID, 4, 0),()),
		"RelativeSize": ((2004, LCID, 4, 0),()),
		"StartValue": ((2010, LCID, 4, 0),()),
		"Style": ((2009, LCID, 4, 0),()),
		"Type": ((2008, LCID, 4, 0),()),
		"UseTextColor": ((2005, LCID, 4, 0),()),
		"UseTextFont": ((2006, LCID, 4, 0),()),
		"Visible": ((0, LCID, 4, 0),()),
	}
	# Default property for this class is 'Visible'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (3, 0), (), "Visible", None))
	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class CalloutFormat(DispatchBaseClass):
	CLSID = IID('{91493485-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def AutomaticLength(self):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), (),)

	def CustomDrop(self, Drop=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((4, 1),),Drop
			)

	def CustomLength(self, Length=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((4, 1),),Length
			)

	def PresetDrop(self, DropType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((3, 1),),DropType
			)

	_prop_map_get_ = {
		"Accent": (100, 2, (3, 0), (), "Accent", None),
		"Angle": (101, 2, (3, 0), (), "Angle", None),
		"Application": (2001, 2, (9, 0), (), "Application", None),
		"AutoAttach": (102, 2, (3, 0), (), "AutoAttach", None),
		"AutoLength": (103, 2, (3, 0), (), "AutoLength", None),
		"Border": (104, 2, (3, 0), (), "Border", None),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		"Drop": (105, 2, (4, 0), (), "Drop", None),
		"DropType": (106, 2, (3, 0), (), "DropType", None),
		"Gap": (107, 2, (4, 0), (), "Gap", None),
		"Length": (108, 2, (4, 0), (), "Length", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		"Type": (109, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Accent": ((100, LCID, 4, 0),()),
		"Angle": ((101, LCID, 4, 0),()),
		"AutoAttach": ((102, LCID, 4, 0),()),
		"Border": ((104, LCID, 4, 0),()),
		"Gap": ((107, LCID, 4, 0),()),
		"Type": ((109, LCID, 4, 0),()),
	}

class CanvasShapes(DispatchBaseClass):
	CLSID = IID('{914934EC-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type Shape
	def AddCallout(self, Type=defaultNamedNotOptArg, Left=defaultNamedNotOptArg, Top=defaultNamedNotOptArg, Width=defaultNamedNotOptArg
			, Height=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), ((3, 1), (4, 1), (4, 1), (4, 1), (4, 1)),Type
			, Left, Top, Width, Height)
		if ret is not None:
			ret = Dispatch(ret, 'AddCallout', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddConnector(self, Type=defaultNamedNotOptArg, BeginX=defaultNamedNotOptArg, BeginY=defaultNamedNotOptArg, EndX=defaultNamedNotOptArg
			, EndY=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), ((3, 1), (4, 1), (4, 1), (4, 1), (4, 1)),Type
			, BeginX, BeginY, EndX, EndY)
		if ret is not None:
			ret = Dispatch(ret, 'AddConnector', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddCurve(self, SafeArrayOfPoints=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(12, LCID, 1, (9, 0), ((12, 1),),SafeArrayOfPoints
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddCurve', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddLabel(self, Orientation=defaultNamedNotOptArg, Left=defaultNamedNotOptArg, Top=defaultNamedNotOptArg, Width=defaultNamedNotOptArg
			, Height=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), ((3, 1), (4, 1), (4, 1), (4, 1), (4, 1)),Orientation
			, Left, Top, Width, Height)
		if ret is not None:
			ret = Dispatch(ret, 'AddLabel', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddLine(self, BeginX=defaultNamedNotOptArg, BeginY=defaultNamedNotOptArg, EndX=defaultNamedNotOptArg, EndY=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), ((4, 1), (4, 1), (4, 1), (4, 1)),BeginX
			, BeginY, EndX, EndY)
		if ret is not None:
			ret = Dispatch(ret, 'AddLine', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddPicture(self, FileName=defaultNamedNotOptArg, LinkToFile=defaultNamedNotOptArg, SaveWithDocument=defaultNamedNotOptArg, Left=defaultNamedNotOptArg
			, Top=defaultNamedNotOptArg, Width=-1.0, Height=-1.0):
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), ((8, 1), (3, 1), (3, 1), (4, 1), (4, 1), (4, 49), (4, 49)),FileName
			, LinkToFile, SaveWithDocument, Left, Top, Width
			, Height)
		if ret is not None:
			ret = Dispatch(ret, 'AddPicture', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddPolyline(self, SafeArrayOfPoints=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(16, LCID, 1, (9, 0), ((12, 1),),SafeArrayOfPoints
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddPolyline', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddShape(self, Type=defaultNamedNotOptArg, Left=defaultNamedNotOptArg, Top=defaultNamedNotOptArg, Width=defaultNamedNotOptArg
			, Height=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), ((3, 1), (4, 1), (4, 1), (4, 1), (4, 1)),Type
			, Left, Top, Width, Height)
		if ret is not None:
			ret = Dispatch(ret, 'AddShape', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddTextEffect(self, PresetTextEffect=defaultNamedNotOptArg, Text=defaultNamedNotOptArg, FontName=defaultNamedNotOptArg, FontSize=defaultNamedNotOptArg
			, FontBold=defaultNamedNotOptArg, FontItalic=defaultNamedNotOptArg, Left=defaultNamedNotOptArg, Top=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(18, LCID, 1, (9, 0), ((3, 1), (8, 1), (8, 1), (4, 1), (3, 1), (3, 1), (4, 1), (4, 1)),PresetTextEffect
			, Text, FontName, FontSize, FontBold, FontItalic
			, Left, Top)
		if ret is not None:
			ret = Dispatch(ret, 'AddTextEffect', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddTextbox(self, Orientation=defaultNamedNotOptArg, Left=defaultNamedNotOptArg, Top=defaultNamedNotOptArg, Width=defaultNamedNotOptArg
			, Height=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(19, LCID, 1, (9, 0), ((3, 1), (4, 1), (4, 1), (4, 1), (4, 1)),Orientation
			, Left, Top, Width, Height)
		if ret is not None:
			ret = Dispatch(ret, 'AddTextbox', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type FreeformBuilder
	def BuildFreeform(self, EditingType=defaultNamedNotOptArg, X1=defaultNamedNotOptArg, Y1=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(20, LCID, 1, (9, 0), ((3, 1), (4, 1), (4, 1)),EditingType
			, X1, Y1)
		if ret is not None:
			ret = Dispatch(ret, 'BuildFreeform', '{91493478-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type ShapeRange
	def Range(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(21, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Range', '{9149347A-5A91-11CF-8700-00AA0060263B}')
		return ret

	def SelectAll(self):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Application": (2001, 2, (9, 0), (), "Application", None),
		# Method 'Background' returns object of type 'Shape'
		"Background": (100, 2, (9, 0), (), "Background", '{91493479-5A91-11CF-8700-00AA0060263B}'),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{91493479-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{91493479-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class Cell(DispatchBaseClass):
	CLSID = IID('{914934C9-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Merge(self, MergeTo=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2005, LCID, 1, (24, 0), ((9, 1),),MergeTo
			)

	def Select(self):
		return self._oleobj_.InvokeTypes(2007, LCID, 1, (24, 0), (),)

	def Split(self, NumRows=defaultNamedNotOptArg, NumColumns=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2006, LCID, 1, (24, 0), ((3, 1), (3, 1)),NumRows
			, NumColumns)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Borders' returns object of type 'Borders'
		"Borders": (2004, 2, (9, 0), (), "Borders", '{914934CA-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Selected": (2008, 2, (11, 0), (), "Selected", None),
		# Method 'Shape' returns object of type 'Shape'
		"Shape": (2003, 2, (9, 0), (), "Shape", '{91493479-5A91-11CF-8700-00AA0060263B}'),
	}
	_prop_map_put_ = {
	}

class CellRange(DispatchBaseClass):
	CLSID = IID('{914934C8-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type Cell
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{914934C9-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Borders' returns object of type 'Borders'
		"Borders": (2003, 2, (9, 0), (), "Borders", '{914934CA-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{914934C9-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{914934C9-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{914934C9-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class Collection(DispatchBaseClass):
	CLSID = IID('{91493450-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Count": (11, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, None)
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),None)
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class ColorEffect(DispatchBaseClass):
	CLSID = IID('{914934E6-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		# Method 'By' returns object of type 'ColorFormat'
		"By": (2003, 2, (9, 0), (), "By", '{91493452-5A91-11CF-8700-00AA0060263B}'),
		# Method 'From' returns object of type 'ColorFormat'
		"From": (2004, 2, (9, 0), (), "From", '{91493452-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		# Method 'To' returns object of type 'ColorFormat'
		"To": (2005, 2, (9, 0), (), "To", '{91493452-5A91-11CF-8700-00AA0060263B}'),
	}
	_prop_map_put_ = {
	}

class ColorFormat(DispatchBaseClass):
	CLSID = IID('{91493452-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Application": (2001, 2, (9, 0), (), "Application", None),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		"RGB": (0, 2, (3, 0), (), "RGB", None),
		"SchemeColor": (2003, 2, (3, 0), (), "SchemeColor", None),
		"TintAndShade": (103, 2, (4, 0), (), "TintAndShade", None),
		"Type": (101, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"RGB": ((0, LCID, 4, 0),()),
		"SchemeColor": ((2003, LCID, 4, 0),()),
		"TintAndShade": ((103, LCID, 4, 0),()),
	}
	# Default property for this class is 'RGB'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (3, 0), (), "RGB", None))
	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class ColorScheme(DispatchBaseClass):
	CLSID = IID('{9149346F-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type RGBColor
	def Colors(self, SchemeColor=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),SchemeColor
			)
		if ret is not None:
			ret = Dispatch(ret, 'Colors', '{91493470-5A91-11CF-8700-00AA0060263B}')
		return ret

	def Delete(self):
		return self._oleobj_.InvokeTypes(2003, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Colors'
	def __call__(self, SchemeColor=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),SchemeColor
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{91493470-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, None)
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),None)
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class ColorSchemes(DispatchBaseClass):
	CLSID = IID('{9149346E-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type ColorScheme
	def Add(self, Scheme=0):
		ret = self._oleobj_.InvokeTypes(2003, LCID, 1, (9, 0), ((9, 49),),Scheme
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{9149346F-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type ColorScheme
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{9149346F-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{9149346F-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{9149346F-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{9149346F-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class Column(DispatchBaseClass):
	CLSID = IID('{914934C5-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Delete(self):
		return self._oleobj_.InvokeTypes(2005, LCID, 1, (24, 0), (),)

	def Select(self):
		return self._oleobj_.InvokeTypes(2004, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Cells' returns object of type 'CellRange'
		"Cells": (2003, 2, (9, 0), (), "Cells", '{914934C8-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Width": (2006, 2, (4, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"Width": ((2006, LCID, 4, 0),()),
	}

class Columns(DispatchBaseClass):
	CLSID = IID('{914934C4-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type Column
	def Add(self, BeforeColumn=-1):
		ret = self._oleobj_.InvokeTypes(2003, LCID, 1, (9, 0), ((3, 49),),BeforeColumn
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{914934C5-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Column
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{914934C5-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{914934C5-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{914934C5-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{914934C5-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class CommandEffect(DispatchBaseClass):
	CLSID = IID('{914934EF-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Command": (2004, 2, (8, 0), (), "Command", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Type": (2003, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Command": ((2004, LCID, 4, 0),()),
		"Type": ((2003, LCID, 4, 0),()),
	}

class Comment(DispatchBaseClass):
	CLSID = IID('{914934D5-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Delete(self):
		return self._oleobj_.InvokeTypes(2010, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Author": (2003, 2, (8, 0), (), "Author", None),
		"AuthorIndex": (2007, 2, (3, 0), (), "AuthorIndex", None),
		"AuthorInitials": (2004, 2, (8, 0), (), "AuthorInitials", None),
		"DateTime": (2006, 2, (7, 0), (), "DateTime", None),
		"Left": (2008, 2, (4, 0), (), "Left", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Text": (2005, 2, (8, 0), (), "Text", None),
		"Top": (2009, 2, (4, 0), (), "Top", None),
	}
	_prop_map_put_ = {
	}

class Comments(DispatchBaseClass):
	CLSID = IID('{914934D4-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type Comment
	def Add(self, Left=defaultNamedNotOptArg, Top=defaultNamedNotOptArg, Author=defaultNamedNotOptArg, AuthorInitials=defaultNamedNotOptArg
			, Text=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(2003, LCID, 1, (9, 0), ((4, 1), (4, 1), (8, 1), (8, 1), (8, 1)),Left
			, Top, Author, AuthorInitials, Text)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{914934D5-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Comment
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{914934D5-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{914934D5-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{914934D5-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{914934D5-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class ConnectorFormat(DispatchBaseClass):
	CLSID = IID('{91493481-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def BeginConnect(self, ConnectedShape=defaultNamedNotOptArg, ConnectionSite=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((9, 1), (3, 1)),ConnectedShape
			, ConnectionSite)

	def BeginDisconnect(self):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	def EndConnect(self, ConnectedShape=defaultNamedNotOptArg, ConnectionSite=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((9, 1), (3, 1)),ConnectedShape
			, ConnectionSite)

	def EndDisconnect(self):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Application": (2001, 2, (9, 0), (), "Application", None),
		"BeginConnected": (100, 2, (3, 0), (), "BeginConnected", None),
		# Method 'BeginConnectedShape' returns object of type 'Shape'
		"BeginConnectedShape": (101, 2, (9, 0), (), "BeginConnectedShape", '{91493479-5A91-11CF-8700-00AA0060263B}'),
		"BeginConnectionSite": (102, 2, (3, 0), (), "BeginConnectionSite", None),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		"EndConnected": (103, 2, (3, 0), (), "EndConnected", None),
		# Method 'EndConnectedShape' returns object of type 'Shape'
		"EndConnectedShape": (104, 2, (9, 0), (), "EndConnectedShape", '{91493479-5A91-11CF-8700-00AA0060263B}'),
		"EndConnectionSite": (105, 2, (3, 0), (), "EndConnectionSite", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		"Type": (106, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Type": ((106, LCID, 4, 0),()),
	}

class DefaultWebOptions(DispatchBaseClass):
	CLSID = IID('{914934CD-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		"AllowPNG": (2008, 2, (3, 0), (), "AllowPNG", None),
		"AlwaysSaveInDefaultEncoding": (2013, 2, (3, 0), (), "AlwaysSaveInDefaultEncoding", None),
		"CheckIfOfficeIsHTMLEditor": (2012, 2, (3, 0), (), "CheckIfOfficeIsHTMLEditor", None),
		"Encoding": (2010, 2, (3, 0), (), "Encoding", None),
		"FolderSuffix": (2015, 2, (8, 0), (), "FolderSuffix", None),
		# Method 'Fonts' returns object of type 'WebPageFonts'
		"Fonts": (2014, 2, (9, 0), (), "Fonts", '{000C0914-0000-0000-C000-000000000046}'),
		"FrameColors": (2002, 2, (3, 0), (), "FrameColors", None),
		"HTMLVersion": (2018, 2, (3, 0), (), "HTMLVersion", None),
		"IncludeNavigation": (2001, 2, (3, 0), (), "IncludeNavigation", None),
		"OrganizeInFolder": (2005, 2, (3, 0), (), "OrganizeInFolder", None),
		"RelyOnVML": (2007, 2, (3, 0), (), "RelyOnVML", None),
		"ResizeGraphics": (2003, 2, (3, 0), (), "ResizeGraphics", None),
		"SaveNewWebPagesAsWebArchives": (2017, 2, (3, 0), (), "SaveNewWebPagesAsWebArchives", None),
		"ScreenSize": (2009, 2, (3, 0), (), "ScreenSize", None),
		"ShowSlideAnimation": (2004, 2, (3, 0), (), "ShowSlideAnimation", None),
		"TargetBrowser": (2016, 2, (3, 0), (), "TargetBrowser", None),
		"UpdateLinksOnSave": (2011, 2, (3, 0), (), "UpdateLinksOnSave", None),
		"UseLongFileNames": (2006, 2, (3, 0), (), "UseLongFileNames", None),
	}
	_prop_map_put_ = {
		"AllowPNG": ((2008, LCID, 4, 0),()),
		"AlwaysSaveInDefaultEncoding": ((2013, LCID, 4, 0),()),
		"CheckIfOfficeIsHTMLEditor": ((2012, LCID, 4, 0),()),
		"Encoding": ((2010, LCID, 4, 0),()),
		"FrameColors": ((2002, LCID, 4, 0),()),
		"HTMLVersion": ((2018, LCID, 4, 0),()),
		"IncludeNavigation": ((2001, LCID, 4, 0),()),
		"OrganizeInFolder": ((2005, LCID, 4, 0),()),
		"RelyOnVML": ((2007, LCID, 4, 0),()),
		"ResizeGraphics": ((2003, LCID, 4, 0),()),
		"SaveNewWebPagesAsWebArchives": ((2017, LCID, 4, 0),()),
		"ScreenSize": ((2009, LCID, 4, 0),()),
		"ShowSlideAnimation": ((2004, LCID, 4, 0),()),
		"TargetBrowser": ((2016, LCID, 4, 0),()),
		"UpdateLinksOnSave": ((2011, LCID, 4, 0),()),
		"UseLongFileNames": ((2006, LCID, 4, 0),()),
	}

class Design(DispatchBaseClass):
	CLSID = IID('{914934D7-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type _Master
	def AddTitleMaster(self):
		ret = self._oleobj_.InvokeTypes(2006, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'AddTitleMaster', '{9149346C-5A91-11CF-8700-00AA0060263B}')
		return ret

	def Delete(self):
		return self._oleobj_.InvokeTypes(2011, LCID, 1, (24, 0), (),)

	def MoveTo(self, toPos=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2010, LCID, 1, (24, 0), ((3, 1),),toPos
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"HasTitleMaster": (2005, 2, (3, 0), (), "HasTitleMaster", None),
		"Index": (2007, 2, (3, 0), (), "Index", None),
		"Name": (2008, 2, (8, 0), (), "Name", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Preserved": (2009, 2, (3, 0), (), "Preserved", None),
		# Method 'SlideMaster' returns object of type '_Master'
		"SlideMaster": (2003, 2, (9, 0), (), "SlideMaster", '{9149346C-5A91-11CF-8700-00AA0060263B}'),
		# Method 'TitleMaster' returns object of type '_Master'
		"TitleMaster": (2004, 2, (9, 0), (), "TitleMaster", '{9149346C-5A91-11CF-8700-00AA0060263B}'),
	}
	_prop_map_put_ = {
		"Name": ((2008, LCID, 4, 0),()),
		"Preserved": ((2009, LCID, 4, 0),()),
	}

class Designs(DispatchBaseClass):
	CLSID = IID('{914934D6-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type Design
	def Add(self, designName=defaultNamedNotOptArg, Index=-1):
		ret = self._oleobj_.InvokeTypes(2003, LCID, 1, (9, 0), ((8, 1), (3, 49)),designName
			, Index)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{914934D7-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Design
	def Clone(self, pOriginal=defaultNamedNotOptArg, Index=-1):
		ret = self._oleobj_.InvokeTypes(2005, LCID, 1, (9, 0), ((9, 1), (3, 49)),pOriginal
			, Index)
		if ret is not None:
			ret = Dispatch(ret, 'Clone', '{914934D7-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Design
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{914934D7-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Design
	def Load(self, TemplateName=defaultNamedNotOptArg, Index=-1):
		ret = self._oleobj_.InvokeTypes(2004, LCID, 1, (9, 0), ((8, 1), (3, 49)),TemplateName
			, Index)
		if ret is not None:
			ret = Dispatch(ret, 'Load', '{914934D7-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{914934D7-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{914934D7-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{914934D7-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class Diagram(DispatchBaseClass):
	CLSID = IID('{914934DB-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Convert(self, Type=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((3, 1),),Type
			)

	def FitText(self):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Application": (2001, 2, (9, 0), (), "Application", None),
		"AutoFormat": (105, 2, (3, 0), (), "AutoFormat", None),
		"AutoLayout": (103, 2, (3, 0), (), "AutoLayout", None),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		# Method 'Nodes' returns object of type 'DiagramNodes'
		"Nodes": (101, 2, (9, 0), (), "Nodes", '{914934DA-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (100, 2, (9, 0), (), "Parent", None),
		"Reverse": (104, 2, (3, 0), (), "Reverse", None),
		"Type": (102, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"AutoFormat": ((105, LCID, 4, 0),()),
		"AutoLayout": ((103, LCID, 4, 0),()),
		"Reverse": ((104, LCID, 4, 0),()),
	}

class DiagramNode(DispatchBaseClass):
	CLSID = IID('{914934D8-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type DiagramNode
	def AddNode(self, Pos=2, NodeType=1):
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), ((3, 49), (3, 49)),Pos
			, NodeType)
		if ret is not None:
			ret = Dispatch(ret, 'AddNode', '{914934D8-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type DiagramNode
	def CloneNode(self, CopyChildren=defaultNamedNotOptArg, TargetNode=defaultNamedNotOptArg, Pos=2):
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), ((11, 1), (9, 1), (3, 49)),CopyChildren
			, TargetNode, Pos)
		if ret is not None:
			ret = Dispatch(ret, 'CloneNode', '{914934D8-5A91-11CF-8700-00AA0060263B}')
		return ret

	def Delete(self):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	def MoveNode(self, TargetNode=defaultNamedNotOptArg, Pos=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((9, 1), (3, 1)),TargetNode
			, Pos)

	# Result is of type DiagramNode
	def NextNode(self):
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'NextNode', '{914934D8-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type DiagramNode
	def PrevNode(self):
		ret = self._oleobj_.InvokeTypes(18, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'PrevNode', '{914934D8-5A91-11CF-8700-00AA0060263B}')
		return ret

	def ReplaceNode(self, TargetNode=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((9, 1),),TargetNode
			)

	def SwapNode(self, TargetNode=defaultNamedNotOptArg, SwapChildren=True):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((9, 1), (11, 49)),TargetNode
			, SwapChildren)

	def TransferChildren(self, ReceivingNode=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((9, 1),),ReceivingNode
			)

	_prop_map_get_ = {
		"Application": (2001, 2, (9, 0), (), "Application", None),
		# Method 'Children' returns object of type 'DiagramNodeChildren'
		"Children": (101, 2, (9, 0), (), "Children", '{914934D9-5A91-11CF-8700-00AA0060263B}'),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		# Method 'Diagram' returns object of type 'Diagram'
		"Diagram": (104, 2, (9, 0), (), "Diagram", '{914934DB-5A91-11CF-8700-00AA0060263B}'),
		"Layout": (105, 2, (3, 0), (), "Layout", None),
		"Parent": (100, 2, (9, 0), (), "Parent", None),
		# Method 'Root' returns object of type 'DiagramNode'
		"Root": (103, 2, (9, 0), (), "Root", '{914934D8-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Shape' returns object of type 'Shape'
		"Shape": (102, 2, (9, 0), (), "Shape", '{91493479-5A91-11CF-8700-00AA0060263B}'),
		# Method 'TextShape' returns object of type 'Shape'
		"TextShape": (106, 2, (9, 0), (), "TextShape", '{91493479-5A91-11CF-8700-00AA0060263B}'),
	}
	_prop_map_put_ = {
		"Layout": ((105, LCID, 4, 0),()),
	}

class DiagramNodeChildren(DispatchBaseClass):
	CLSID = IID('{914934D9-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type DiagramNode
	def AddNode(self, Index=-1, NodeType=1):
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), ((12, 49), (3, 49)),Index
			, NodeType)
		if ret is not None:
			ret = Dispatch(ret, 'AddNode', '{914934D8-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type DiagramNode
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{914934D8-5A91-11CF-8700-00AA0060263B}')
		return ret

	def SelectAll(self):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Application": (2001, 2, (9, 0), (), "Application", None),
		"Count": (101, 2, (3, 0), (), "Count", None),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		# Method 'FirstChild' returns object of type 'DiagramNode'
		"FirstChild": (103, 2, (9, 0), (), "FirstChild", '{914934D8-5A91-11CF-8700-00AA0060263B}'),
		# Method 'LastChild' returns object of type 'DiagramNode'
		"LastChild": (104, 2, (9, 0), (), "LastChild", '{914934D8-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (100, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{914934D8-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{914934D8-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{914934D8-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(101, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class DiagramNodes(DispatchBaseClass):
	CLSID = IID('{914934DA-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type DiagramNode
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{914934D8-5A91-11CF-8700-00AA0060263B}')
		return ret

	def SelectAll(self):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Application": (2001, 2, (9, 0), (), "Application", None),
		"Count": (101, 2, (3, 0), (), "Count", None),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		"Parent": (100, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{914934D8-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{914934D8-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{914934D8-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(101, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class DocumentWindow(DispatchBaseClass):
	CLSID = IID('{91493457-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Activate(self):
		return self._oleobj_.InvokeTypes(2015, LCID, 1, (24, 0), (),)

	def Close(self):
		return self._oleobj_.InvokeTypes(2019, LCID, 1, (24, 0), (),)

	def FitToPage(self):
		return self._oleobj_.InvokeTypes(2014, LCID, 1, (24, 0), (),)

	def LargeScroll(self, Down=1, Up=0, ToRight=0, ToLeft=0):
		return self._oleobj_.InvokeTypes(2016, LCID, 1, (24, 0), ((3, 49), (3, 49), (3, 49), (3, 49)),Down
			, Up, ToRight, ToLeft)

	# Result is of type DocumentWindow
	def NewWindow(self):
		ret = self._oleobj_.InvokeTypes(2018, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'NewWindow', '{91493457-5A91-11CF-8700-00AA0060263B}')
		return ret

	def PointsToScreenPixelsX(self, Points=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2026, LCID, 1, (3, 0), ((4, 1),),Points
			)

	def PointsToScreenPixelsY(self, Points=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2027, LCID, 1, (3, 0), ((4, 1),),Points
			)

	def RangeFromPoint(self, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(2025, LCID, 1, (9, 0), ((3, 1), (3, 1)),X
			, Y)
		if ret is not None:
			ret = Dispatch(ret, 'RangeFromPoint', None)
		return ret

	def ScrollIntoView(self, Left=defaultNamedNotOptArg, Top=defaultNamedNotOptArg, Width=defaultNamedNotOptArg, Height=defaultNamedNotOptArg
			, Start=-1):
		return self._oleobj_.InvokeTypes(2028, LCID, 1, (24, 0), ((4, 1), (4, 1), (4, 1), (4, 1), (3, 49)),Left
			, Top, Width, Height, Start)

	def SmallScroll(self, Down=1, Up=0, ToRight=0, ToLeft=0):
		return self._oleobj_.InvokeTypes(2017, LCID, 1, (24, 0), ((3, 49), (3, 49), (3, 49), (3, 49)),Down
			, Up, ToRight, ToLeft)

	_prop_map_get_ = {
		"Active": (2008, 2, (3, 0), (), "Active", None),
		# Method 'ActivePane' returns object of type 'Pane'
		"ActivePane": (2021, 2, (9, 0), (), "ActivePane", '{914934CC-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"BlackAndWhite": (2007, 2, (3, 0), (), "BlackAndWhite", None),
		"Caption": (0, 2, (8, 0), (), "Caption", None),
		"HWND": (2020, 2, (3, 0), (), "HWND", None),
		"Height": (2013, 2, (4, 0), (), "Height", None),
		"Left": (2010, 2, (4, 0), (), "Left", None),
		# Method 'Panes' returns object of type 'Panes'
		"Panes": (2022, 2, (9, 0), (), "Panes", '{914934CB-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		# Method 'Presentation' returns object of type 'Presentation'
		"Presentation": (2005, 2, (13, 0), (), "Presentation", '{91493444-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Selection' returns object of type 'Selection'
		"Selection": (2003, 2, (9, 0), (), "Selection", '{91493454-5A91-11CF-8700-00AA0060263B}'),
		"SplitHorizontal": (2024, 2, (3, 0), (), "SplitHorizontal", None),
		"SplitVertical": (2023, 2, (3, 0), (), "SplitVertical", None),
		"Top": (2011, 2, (4, 0), (), "Top", None),
		# Method 'View' returns object of type 'View'
		"View": (2004, 2, (9, 0), (), "View", '{91493458-5A91-11CF-8700-00AA0060263B}'),
		"ViewType": (2006, 2, (3, 0), (), "ViewType", None),
		"Width": (2012, 2, (4, 0), (), "Width", None),
		"WindowState": (2009, 2, (3, 0), (), "WindowState", None),
	}
	_prop_map_put_ = {
		"BlackAndWhite": ((2007, LCID, 4, 0),()),
		"Height": ((2013, LCID, 4, 0),()),
		"Left": ((2010, LCID, 4, 0),()),
		"SplitHorizontal": ((2024, LCID, 4, 0),()),
		"SplitVertical": ((2023, LCID, 4, 0),()),
		"Top": ((2011, LCID, 4, 0),()),
		"ViewType": ((2006, LCID, 4, 0),()),
		"Width": ((2012, LCID, 4, 0),()),
		"WindowState": ((2009, LCID, 4, 0),()),
	}
	# Default property for this class is 'Caption'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Caption", None))
	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class DocumentWindows(DispatchBaseClass):
	CLSID = IID('{91493455-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Arrange(self, arrangeStyle=1):
		return self._oleobj_.InvokeTypes(2003, LCID, 1, (24, 0), ((3, 49),),arrangeStyle
			)

	# Result is of type DocumentWindow
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{91493457-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{91493457-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{91493457-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{91493457-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class EApplication:
	CLSID = CLSID_Sink = IID('{914934C2-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = IID('{91493441-5A91-11CF-8700-00AA0060263B}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		     2018 : "OnPresentationBeforeSave",
		     2017 : "OnColorSchemeChanged",
		     2013 : "OnSlideShowNextSlide",
		     2019 : "OnSlideShowNextClick",
		     2006 : "OnPresentationOpen",
		     2005 : "OnPresentationSave",
		     2002 : "OnWindowBeforeRightClick",
		     2011 : "OnSlideShowBegin",
		     2003 : "OnWindowBeforeDoubleClick",
		     2001 : "OnWindowSelectionChange",
		     2007 : "OnNewPresentation",
		     2010 : "OnWindowDeactivate",
		     2004 : "OnPresentationClose",
		     2021 : "OnAfterPresentationOpen",
		     2020 : "OnAfterNewPresentation",
		     2012 : "OnSlideShowNextBuild",
		     2008 : "OnPresentationNewSlide",
		     2022 : "OnPresentationSync",
		     2016 : "OnSlideSelectionChanged",
		     2009 : "OnWindowActivate",
		     2014 : "OnSlideShowEnd",
		     2015 : "OnPresentationPrint",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(global_IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except global_com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnPresentationBeforeSave(self, Pres=defaultNamedNotOptArg, Cancel=defaultNamedNotOptArg):
#	def OnColorSchemeChanged(self, SldRange=defaultNamedNotOptArg):
#	def OnSlideShowNextSlide(self, Wn=defaultNamedNotOptArg):
#	def OnSlideShowNextClick(self, Wn=defaultNamedNotOptArg, nEffect=defaultNamedNotOptArg):
#	def OnPresentationOpen(self, Pres=defaultNamedNotOptArg):
#	def OnPresentationSave(self, Pres=defaultNamedNotOptArg):
#	def OnWindowBeforeRightClick(self, Sel=defaultNamedNotOptArg, Cancel=defaultNamedNotOptArg):
#	def OnSlideShowBegin(self, Wn=defaultNamedNotOptArg):
#	def OnWindowBeforeDoubleClick(self, Sel=defaultNamedNotOptArg, Cancel=defaultNamedNotOptArg):
#	def OnWindowSelectionChange(self, Sel=defaultNamedNotOptArg):
#	def OnNewPresentation(self, Pres=defaultNamedNotOptArg):
#	def OnWindowDeactivate(self, Pres=defaultNamedNotOptArg, Wn=defaultNamedNotOptArg):
#	def OnPresentationClose(self, Pres=defaultNamedNotOptArg):
#	def OnAfterPresentationOpen(self, Pres=defaultNamedNotOptArg):
#	def OnAfterNewPresentation(self, Pres=defaultNamedNotOptArg):
#	def OnSlideShowNextBuild(self, Wn=defaultNamedNotOptArg):
#	def OnPresentationNewSlide(self, Sld=defaultNamedNotOptArg):
#	def OnPresentationSync(self, Pres=defaultNamedNotOptArg, SyncEventType=defaultNamedNotOptArg):
#	def OnSlideSelectionChanged(self, SldRange=defaultNamedNotOptArg):
#	def OnWindowActivate(self, Pres=defaultNamedNotOptArg, Wn=defaultNamedNotOptArg):
#	def OnSlideShowEnd(self, Pres=defaultNamedNotOptArg):
#	def OnPresentationPrint(self, Pres=defaultNamedNotOptArg):


class Effect(DispatchBaseClass):
	CLSID = IID('{914934DF-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Delete(self):
		return self._oleobj_.InvokeTypes(2007, LCID, 1, (24, 0), (),)

	def MoveAfter(self, Effect=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2006, LCID, 1, (24, 0), ((9, 1),),Effect
			)

	def MoveBefore(self, Effect=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2005, LCID, 1, (24, 0), ((9, 1),),Effect
			)

	def MoveTo(self, toPos=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2004, LCID, 1, (24, 0), ((3, 1),),toPos
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Behaviors' returns object of type 'AnimationBehaviors'
		"Behaviors": (2017, 2, (9, 0), (), "Behaviors", '{914934E3-5A91-11CF-8700-00AA0060263B}'),
		"DisplayName": (2015, 2, (8, 0), (), "DisplayName", None),
		# Method 'EffectInformation' returns object of type 'EffectInformation'
		"EffectInformation": (2018, 2, (9, 0), (), "EffectInformation", '{914934E2-5A91-11CF-8700-00AA0060263B}'),
		# Method 'EffectParameters' returns object of type 'EffectParameters'
		"EffectParameters": (2011, 2, (9, 0), (), "EffectParameters", '{914934E1-5A91-11CF-8700-00AA0060263B}'),
		"EffectType": (2010, 2, (3, 0), (), "EffectType", None),
		"Exit": (2016, 2, (3, 0), (), "Exit", None),
		"Index": (2008, 2, (3, 0), (), "Index", None),
		"Paragraph": (2014, 2, (3, 0), (), "Paragraph", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		# Method 'Shape' returns object of type 'Shape'
		"Shape": (2003, 2, (9, 0), (), "Shape", '{91493479-5A91-11CF-8700-00AA0060263B}'),
		"TextRangeLength": (2013, 2, (3, 0), (), "TextRangeLength", None),
		"TextRangeStart": (2012, 2, (3, 0), (), "TextRangeStart", None),
		# Method 'Timing' returns object of type 'Timing'
		"Timing": (2009, 2, (9, 0), (), "Timing", '{914934E0-5A91-11CF-8700-00AA0060263B}'),
	}
	_prop_map_put_ = {
		"EffectType": ((2010, LCID, 4, 0),()),
		"Exit": ((2016, LCID, 4, 0),()),
		"Paragraph": ((2014, LCID, 4, 0),()),
		"Shape": ((2003, LCID, 4, 0),()),
	}

class EffectInformation(DispatchBaseClass):
	CLSID = IID('{914934E2-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		"AfterEffect": (2003, 2, (3, 0), (), "AfterEffect", None),
		"AnimateBackground": (2004, 2, (3, 0), (), "AnimateBackground", None),
		"AnimateTextInReverse": (2005, 2, (3, 0), (), "AnimateTextInReverse", None),
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"BuildByLevelEffect": (2006, 2, (3, 0), (), "BuildByLevelEffect", None),
		# Method 'Dim' returns object of type 'ColorFormat'
		"Dim": (2007, 2, (9, 0), (), "Dim", '{91493452-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		# Method 'PlaySettings' returns object of type 'PlaySettings'
		"PlaySettings": (2008, 2, (9, 0), (), "PlaySettings", '{9149348E-5A91-11CF-8700-00AA0060263B}'),
		# Method 'SoundEffect' returns object of type 'SoundEffect'
		"SoundEffect": (2009, 2, (9, 0), (), "SoundEffect", '{91493472-5A91-11CF-8700-00AA0060263B}'),
		"TextUnitEffect": (2010, 2, (3, 0), (), "TextUnitEffect", None),
	}
	_prop_map_put_ = {
	}

class EffectParameters(DispatchBaseClass):
	CLSID = IID('{914934E1-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Amount": (2004, 2, (4, 0), (), "Amount", None),
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Color2' returns object of type 'ColorFormat'
		"Color2": (2006, 2, (9, 0), (), "Color2", '{91493452-5A91-11CF-8700-00AA0060263B}'),
		"Direction": (2003, 2, (3, 0), (), "Direction", None),
		"FontName": (2008, 2, (8, 0), (), "FontName", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Relative": (2007, 2, (3, 0), (), "Relative", None),
		"Size": (2005, 2, (4, 0), (), "Size", None),
	}
	_prop_map_put_ = {
		"Amount": ((2004, LCID, 4, 0),()),
		"Direction": ((2003, LCID, 4, 0),()),
		"FontName": ((2008, LCID, 4, 0),()),
		"Relative": ((2007, LCID, 4, 0),()),
		"Size": ((2005, LCID, 4, 0),()),
	}

class ExtraColors(DispatchBaseClass):
	CLSID = IID('{91493468-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Add(self, Type=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2003, LCID, 1, (24, 0), ((3, 1),),Type
			)

	def Item(self, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(0, LCID, 1, (3, 0), ((3, 1),),Index
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(0, LCID, 1, (3, 0), ((3, 1),),Index
			)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, None)
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),None)
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class FillFormat(DispatchBaseClass):
	CLSID = IID('{9149347E-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Background(self):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), (),)

	def OneColorGradient(self, Style=defaultNamedNotOptArg, Variant=defaultNamedNotOptArg, Degree=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((3, 1), (3, 1), (4, 1)),Style
			, Variant, Degree)

	def Patterned(self, Pattern=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((3, 1),),Pattern
			)

	def PresetGradient(self, Style=defaultNamedNotOptArg, Variant=defaultNamedNotOptArg, PresetGradientType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),Style
			, Variant, PresetGradientType)

	def PresetTextured(self, PresetTexture=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((3, 1),),PresetTexture
			)

	def Solid(self):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), (),)

	def TwoColorGradient(self, Style=defaultNamedNotOptArg, Variant=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((3, 1), (3, 1)),Style
			, Variant)

	def UserPicture(self, PictureFile=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), ((8, 1),),PictureFile
			)

	def UserTextured(self, TextureFile=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), ((8, 1),),TextureFile
			)

	_prop_map_get_ = {
		"Application": (2001, 2, (9, 0), (), "Application", None),
		# Method 'BackColor' returns object of type 'ColorFormat'
		"BackColor": (100, 2, (9, 0), (), "BackColor", '{91493452-5A91-11CF-8700-00AA0060263B}'),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		# Method 'ForeColor' returns object of type 'ColorFormat'
		"ForeColor": (101, 2, (9, 0), (), "ForeColor", '{91493452-5A91-11CF-8700-00AA0060263B}'),
		"GradientColorType": (102, 2, (3, 0), (), "GradientColorType", None),
		"GradientDegree": (103, 2, (4, 0), (), "GradientDegree", None),
		"GradientStyle": (104, 2, (3, 0), (), "GradientStyle", None),
		"GradientVariant": (105, 2, (3, 0), (), "GradientVariant", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		"Pattern": (106, 2, (3, 0), (), "Pattern", None),
		"PresetGradientType": (107, 2, (3, 0), (), "PresetGradientType", None),
		"PresetTexture": (108, 2, (3, 0), (), "PresetTexture", None),
		"TextureName": (109, 2, (8, 0), (), "TextureName", None),
		"TextureType": (110, 2, (3, 0), (), "TextureType", None),
		"Transparency": (111, 2, (4, 0), (), "Transparency", None),
		"Type": (112, 2, (3, 0), (), "Type", None),
		"Visible": (113, 2, (3, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"BackColor": ((100, LCID, 4, 0),()),
		"ForeColor": ((101, LCID, 4, 0),()),
		"Transparency": ((111, LCID, 4, 0),()),
		"Visible": ((113, LCID, 4, 0),()),
	}

class FilterEffect(DispatchBaseClass):
	CLSID = IID('{914934F0-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Reveal": (2005, 2, (3, 0), (), "Reveal", None),
		"Subtype": (2004, 2, (3, 0), (), "Subtype", None),
		"Type": (2003, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Reveal": ((2005, LCID, 4, 0),()),
		"Subtype": ((2004, LCID, 4, 0),()),
		"Type": ((2003, LCID, 4, 0),()),
	}

class Font(DispatchBaseClass):
	CLSID = IID('{91493495-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"AutoRotateNumbers": (2018, 2, (3, 0), (), "AutoRotateNumbers", None),
		"BaselineOffset": (2011, 2, (4, 0), (), "BaselineOffset", None),
		"Bold": (2004, 2, (3, 0), (), "Bold", None),
		# Method 'Color' returns object of type 'ColorFormat'
		"Color": (2003, 2, (9, 0), (), "Color", '{91493452-5A91-11CF-8700-00AA0060263B}'),
		"Embeddable": (2013, 2, (3, 0), (), "Embeddable", None),
		"Embedded": (2012, 2, (3, 0), (), "Embedded", None),
		"Emboss": (2007, 2, (3, 0), (), "Emboss", None),
		"Italic": (2005, 2, (3, 0), (), "Italic", None),
		"Name": (2015, 2, (8, 0), (), "Name", None),
		"NameAscii": (2017, 2, (8, 0), (), "NameAscii", None),
		"NameComplexScript": (2020, 2, (8, 0), (), "NameComplexScript", None),
		"NameFarEast": (2016, 2, (8, 0), (), "NameFarEast", None),
		"NameOther": (2019, 2, (8, 0), (), "NameOther", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Shadow": (2006, 2, (3, 0), (), "Shadow", None),
		"Size": (2014, 2, (4, 0), (), "Size", None),
		"Subscript": (2009, 2, (3, 0), (), "Subscript", None),
		"Superscript": (2010, 2, (3, 0), (), "Superscript", None),
		"Underline": (2008, 2, (3, 0), (), "Underline", None),
	}
	_prop_map_put_ = {
		"AutoRotateNumbers": ((2018, LCID, 4, 0),()),
		"BaselineOffset": ((2011, LCID, 4, 0),()),
		"Bold": ((2004, LCID, 4, 0),()),
		"Emboss": ((2007, LCID, 4, 0),()),
		"Italic": ((2005, LCID, 4, 0),()),
		"Name": ((2015, LCID, 4, 0),()),
		"NameAscii": ((2017, LCID, 4, 0),()),
		"NameComplexScript": ((2020, LCID, 4, 0),()),
		"NameFarEast": ((2016, LCID, 4, 0),()),
		"NameOther": ((2019, LCID, 4, 0),()),
		"Shadow": ((2006, LCID, 4, 0),()),
		"Size": ((2014, LCID, 4, 0),()),
		"Subscript": ((2009, LCID, 4, 0),()),
		"Superscript": ((2010, LCID, 4, 0),()),
		"Underline": ((2008, LCID, 4, 0),()),
	}

class Fonts(DispatchBaseClass):
	CLSID = IID('{91493467-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type Font
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{91493495-5A91-11CF-8700-00AA0060263B}')
		return ret

	def Replace(self, Original=defaultNamedNotOptArg, Replacement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2003, LCID, 1, (24, 0), ((8, 1), (8, 1)),Original
			, Replacement)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{91493495-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{91493495-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{91493495-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class FreeformBuilder(DispatchBaseClass):
	CLSID = IID('{91493478-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def AddNodes(self, SegmentType=defaultNamedNotOptArg, EditingType=defaultNamedNotOptArg, X1=defaultNamedNotOptArg, Y1=defaultNamedNotOptArg
			, X2=0.0, Y2=0.0, X3=0.0, Y3=0.0):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((3, 1), (3, 1), (4, 1), (4, 1), (4, 49), (4, 49), (4, 49), (4, 49)),SegmentType
			, EditingType, X1, Y1, X2, Y2
			, X3, Y3)

	# Result is of type Shape
	def ConvertToShape(self):
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ConvertToShape', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		"Application": (2001, 2, (9, 0), (), "Application", None),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}

class GroupShapes(DispatchBaseClass):
	CLSID = IID('{9149347B-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type Shape
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type ShapeRange
	def Range(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Range', '{9149347A-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		"Application": (2001, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{91493479-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{91493479-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class HeaderFooter(DispatchBaseClass):
	CLSID = IID('{9149349C-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Format": (2006, 2, (3, 0), (), "Format", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Text": (2004, 2, (8, 0), (), "Text", None),
		"UseFormat": (2005, 2, (3, 0), (), "UseFormat", None),
		"Visible": (2003, 2, (3, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Format": ((2006, LCID, 4, 0),()),
		"Text": ((2004, LCID, 4, 0),()),
		"UseFormat": ((2005, LCID, 4, 0),()),
		"Visible": ((2003, LCID, 4, 0),()),
	}

class HeadersFooters(DispatchBaseClass):
	CLSID = IID('{91493474-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Clear(self):
		return self._oleobj_.InvokeTypes(2008, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		# Method 'DateAndTime' returns object of type 'HeaderFooter'
		"DateAndTime": (2003, 2, (9, 0), (), "DateAndTime", '{9149349C-5A91-11CF-8700-00AA0060263B}'),
		"DisplayOnTitleSlide": (2007, 2, (3, 0), (), "DisplayOnTitleSlide", None),
		# Method 'Footer' returns object of type 'HeaderFooter'
		"Footer": (2006, 2, (9, 0), (), "Footer", '{9149349C-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Header' returns object of type 'HeaderFooter'
		"Header": (2005, 2, (9, 0), (), "Header", '{9149349C-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		# Method 'SlideNumber' returns object of type 'HeaderFooter'
		"SlideNumber": (2004, 2, (9, 0), (), "SlideNumber", '{9149349C-5A91-11CF-8700-00AA0060263B}'),
	}
	_prop_map_put_ = {
		"DisplayOnTitleSlide": ((2007, LCID, 4, 0),()),
	}

class Hyperlink(DispatchBaseClass):
	CLSID = IID('{91493465-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def AddToFavorites(self):
		return self._oleobj_.InvokeTypes(2006, LCID, 1, (24, 0), (),)

	def CreateNewDocument(self, FileName=defaultNamedNotOptArg, EditNow=defaultNamedNotOptArg, Overwrite=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2012, LCID, 1, (24, 0), ((8, 1), (3, 1), (3, 1)),FileName
			, EditNow, Overwrite)

	def Delete(self):
		return self._oleobj_.InvokeTypes(2013, LCID, 1, (24, 0), (),)

	def Follow(self):
		return self._oleobj_.InvokeTypes(2011, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Address": (2004, 2, (8, 0), (), "Address", None),
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"EmailSubject": (2007, 2, (8, 0), (), "EmailSubject", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"ScreenTip": (2008, 2, (8, 0), (), "ScreenTip", None),
		"ShowAndReturn": (2010, 2, (3, 0), (), "ShowAndReturn", None),
		"SubAddress": (2005, 2, (8, 0), (), "SubAddress", None),
		"TextToDisplay": (2009, 2, (8, 0), (), "TextToDisplay", None),
		"Type": (2003, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Address": ((2004, LCID, 4, 0),()),
		"EmailSubject": ((2007, LCID, 4, 0),()),
		"ScreenTip": ((2008, LCID, 4, 0),()),
		"ShowAndReturn": ((2010, LCID, 4, 0),()),
		"SubAddress": ((2005, LCID, 4, 0),()),
		"TextToDisplay": ((2009, LCID, 4, 0),()),
	}

class Hyperlinks(DispatchBaseClass):
	CLSID = IID('{91493464-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type Hyperlink
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{91493465-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{91493465-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{91493465-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{91493465-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class LineFormat(DispatchBaseClass):
	CLSID = IID('{9149347F-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Application": (2001, 2, (9, 0), (), "Application", None),
		# Method 'BackColor' returns object of type 'ColorFormat'
		"BackColor": (100, 2, (9, 0), (), "BackColor", '{91493452-5A91-11CF-8700-00AA0060263B}'),
		"BeginArrowheadLength": (101, 2, (3, 0), (), "BeginArrowheadLength", None),
		"BeginArrowheadStyle": (102, 2, (3, 0), (), "BeginArrowheadStyle", None),
		"BeginArrowheadWidth": (103, 2, (3, 0), (), "BeginArrowheadWidth", None),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		"DashStyle": (104, 2, (3, 0), (), "DashStyle", None),
		"EndArrowheadLength": (105, 2, (3, 0), (), "EndArrowheadLength", None),
		"EndArrowheadStyle": (106, 2, (3, 0), (), "EndArrowheadStyle", None),
		"EndArrowheadWidth": (107, 2, (3, 0), (), "EndArrowheadWidth", None),
		# Method 'ForeColor' returns object of type 'ColorFormat'
		"ForeColor": (108, 2, (9, 0), (), "ForeColor", '{91493452-5A91-11CF-8700-00AA0060263B}'),
		"InsetPen": (114, 2, (3, 0), (), "InsetPen", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		"Pattern": (109, 2, (3, 0), (), "Pattern", None),
		"Style": (110, 2, (3, 0), (), "Style", None),
		"Transparency": (111, 2, (4, 0), (), "Transparency", None),
		"Visible": (112, 2, (3, 0), (), "Visible", None),
		"Weight": (113, 2, (4, 0), (), "Weight", None),
	}
	_prop_map_put_ = {
		"BackColor": ((100, LCID, 4, 0),()),
		"BeginArrowheadLength": ((101, LCID, 4, 0),()),
		"BeginArrowheadStyle": ((102, LCID, 4, 0),()),
		"BeginArrowheadWidth": ((103, LCID, 4, 0),()),
		"DashStyle": ((104, LCID, 4, 0),()),
		"EndArrowheadLength": ((105, LCID, 4, 0),()),
		"EndArrowheadStyle": ((106, LCID, 4, 0),()),
		"EndArrowheadWidth": ((107, LCID, 4, 0),()),
		"ForeColor": ((108, LCID, 4, 0),()),
		"InsetPen": ((114, LCID, 4, 0),()),
		"Pattern": ((109, LCID, 4, 0),()),
		"Style": ((110, LCID, 4, 0),()),
		"Transparency": ((111, LCID, 4, 0),()),
		"Visible": ((112, LCID, 4, 0),()),
		"Weight": ((113, LCID, 4, 0),()),
	}

class LinkFormat(DispatchBaseClass):
	CLSID = IID('{91493489-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Update(self):
		return self._oleobj_.InvokeTypes(2005, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"AutoUpdate": (2004, 2, (3, 0), (), "AutoUpdate", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"SourceFullName": (2003, 2, (8, 0), (), "SourceFullName", None),
	}
	_prop_map_put_ = {
		"AutoUpdate": ((2004, LCID, 4, 0),()),
		"SourceFullName": ((2003, LCID, 4, 0),()),
	}

class MotionEffect(DispatchBaseClass):
	CLSID = IID('{914934E5-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"ByX": (2003, 2, (4, 0), (), "ByX", None),
		"ByY": (2004, 2, (4, 0), (), "ByY", None),
		"FromX": (2005, 2, (4, 0), (), "FromX", None),
		"FromY": (2006, 2, (4, 0), (), "FromY", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Path": (2009, 2, (8, 0), (), "Path", None),
		"ToX": (2007, 2, (4, 0), (), "ToX", None),
		"ToY": (2008, 2, (4, 0), (), "ToY", None),
	}
	_prop_map_put_ = {
		"ByX": ((2003, LCID, 4, 0),()),
		"ByY": ((2004, LCID, 4, 0),()),
		"FromX": ((2005, LCID, 4, 0),()),
		"FromY": ((2006, LCID, 4, 0),()),
		"Path": ((2009, LCID, 4, 0),()),
		"ToX": ((2007, LCID, 4, 0),()),
		"ToY": ((2008, LCID, 4, 0),()),
	}

class NamedSlideShow(DispatchBaseClass):
	CLSID = IID('{9149345C-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Delete(self):
		return self._oleobj_.InvokeTypes(2004, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (2006, 2, (3, 0), (), "Count", None),
		"Name": (2003, 2, (8, 0), (), "Name", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"SlideIDs": (2005, 2, (12, 0), (), "SlideIDs", None),
	}
	_prop_map_put_ = {
	}
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2006, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class NamedSlideShows(DispatchBaseClass):
	CLSID = IID('{9149345B-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type NamedSlideShow
	def Add(self, Name=defaultNamedNotOptArg, safeArrayOfSlideIDs=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(2003, LCID, 1, (9, 0), ((8, 1), (12, 1)),Name
			, safeArrayOfSlideIDs)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{9149345C-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type NamedSlideShow
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{9149345C-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{9149345C-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{9149345C-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{9149345C-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class OCXExtender(DispatchBaseClass):
	CLSID = IID('{914934C0-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = IID('{91493446-5A91-11CF-8700-00AA0060263B}')

	_prop_map_get_ = {
		"AltHTML": (-2147417881, 2, (8, 0), (), "AltHTML", None),
		"Height": (-2147418107, 2, (4, 0), (), "Height", None),
		"Left": (-2147418109, 2, (4, 0), (), "Left", None),
		"Name": (-2147418112, 2, (8, 0), (), "Name", None),
		"Top": (-2147418108, 2, (4, 0), (), "Top", None),
		"Visible": (-2147418105, 2, (11, 0), (), "Visible", None),
		"Width": (-2147418106, 2, (4, 0), (), "Width", None),
		"ZOrderPosition": (-2147417882, 2, (3, 0), (), "ZOrderPosition", None),
	}
	_prop_map_put_ = {
		"AltHTML": ((-2147417881, LCID, 4, 0),()),
		"Height": ((-2147418107, LCID, 4, 0),()),
		"Left": ((-2147418109, LCID, 4, 0),()),
		"Name": ((-2147418112, LCID, 4, 0),()),
		"Top": ((-2147418108, LCID, 4, 0),()),
		"Visible": ((-2147418105, LCID, 4, 0),()),
		"Width": ((-2147418106, LCID, 4, 0),()),
	}

class OCXExtenderEvents:
	CLSID = CLSID_Sink = IID('{914934C1-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = IID('{91493446-5A91-11CF-8700-00AA0060263B}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		-2147417888 : "OnGotFocus",
		-2147417887 : "OnLostFocus",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(global_IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except global_com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnGotFocus(self):
#	def OnLostFocus(self):


class OLEFormat(DispatchBaseClass):
	CLSID = IID('{91493488-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Activate(self):
		return self._oleobj_.InvokeTypes(2008, LCID, 1, (24, 0), (),)

	def DoVerb(self, Index=0):
		return self._oleobj_.InvokeTypes(2007, LCID, 1, (24, 0), ((3, 49),),Index
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"FollowColors": (2006, 2, (3, 0), (), "FollowColors", None),
		"Object": (2004, 2, (9, 0), (), "Object", None),
		# Method 'ObjectVerbs' returns object of type 'ObjectVerbs'
		"ObjectVerbs": (2003, 2, (9, 0), (), "ObjectVerbs", '{9149348A-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"ProgID": (2005, 2, (8, 0), (), "ProgID", None),
	}
	_prop_map_put_ = {
		"FollowColors": ((2006, LCID, 4, 0),()),
	}

class ObjectVerbs(DispatchBaseClass):
	CLSID = IID('{9149348A-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Item(self, Index=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(0, LCID, 1, (8, 0), ((3, 1),),Index
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(0, LCID, 1, (8, 0), ((3, 1),),Index
			)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, None)
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),None)
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class Options(DispatchBaseClass):
	CLSID = IID('{914934EE-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		"DisplayPasteOptions": (2001, 2, (3, 0), (), "DisplayPasteOptions", None),
	}
	_prop_map_put_ = {
		"DisplayPasteOptions": ((2001, LCID, 4, 0),()),
	}

class PageSetup(DispatchBaseClass):
	CLSID = IID('{91493466-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"FirstSlideNumber": (2003, 2, (3, 0), (), "FirstSlideNumber", None),
		"NotesOrientation": (2007, 2, (3, 0), (), "NotesOrientation", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"SlideHeight": (2004, 2, (4, 0), (), "SlideHeight", None),
		"SlideOrientation": (2008, 2, (3, 0), (), "SlideOrientation", None),
		"SlideSize": (2006, 2, (3, 0), (), "SlideSize", None),
		"SlideWidth": (2005, 2, (4, 0), (), "SlideWidth", None),
	}
	_prop_map_put_ = {
		"FirstSlideNumber": ((2003, LCID, 4, 0),()),
		"NotesOrientation": ((2007, LCID, 4, 0),()),
		"SlideHeight": ((2004, LCID, 4, 0),()),
		"SlideOrientation": ((2008, LCID, 4, 0),()),
		"SlideSize": ((2006, LCID, 4, 0),()),
		"SlideWidth": ((2005, LCID, 4, 0),()),
	}

class Pane(DispatchBaseClass):
	CLSID = IID('{914934CC-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Activate(self):
		return self._oleobj_.InvokeTypes(2001, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Active": (2002, 2, (3, 0), (), "Active", None),
		# Method 'Application' returns object of type 'Application'
		"Application": (2003, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2000, 2, (9, 0), (), "Parent", None),
		"ViewType": (2004, 2, (3, 0), (), "ViewType", None),
	}
	_prop_map_put_ = {
	}

class Panes(DispatchBaseClass):
	CLSID = IID('{914934CB-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type Pane
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{914934CC-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{914934CC-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{914934CC-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{914934CC-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class ParagraphFormat(DispatchBaseClass):
	CLSID = IID('{91493496-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Alignment": (2003, 2, (3, 0), (), "Alignment", None),
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"BaseLineAlignment": (2011, 2, (3, 0), (), "BaseLineAlignment", None),
		# Method 'Bullet' returns object of type 'BulletFormat'
		"Bullet": (2004, 2, (9, 0), (), "Bullet", '{91493497-5A91-11CF-8700-00AA0060263B}'),
		"FarEastLineBreakControl": (2012, 2, (3, 0), (), "FarEastLineBreakControl", None),
		"HangingPunctuation": (2014, 2, (3, 0), (), "HangingPunctuation", None),
		"LineRuleAfter": (2006, 2, (3, 0), (), "LineRuleAfter", None),
		"LineRuleBefore": (2005, 2, (3, 0), (), "LineRuleBefore", None),
		"LineRuleWithin": (2007, 2, (3, 0), (), "LineRuleWithin", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"SpaceAfter": (2009, 2, (4, 0), (), "SpaceAfter", None),
		"SpaceBefore": (2008, 2, (4, 0), (), "SpaceBefore", None),
		"SpaceWithin": (2010, 2, (4, 0), (), "SpaceWithin", None),
		"TextDirection": (2015, 2, (3, 0), (), "TextDirection", None),
		"WordWrap": (2013, 2, (3, 0), (), "WordWrap", None),
	}
	_prop_map_put_ = {
		"Alignment": ((2003, LCID, 4, 0),()),
		"BaseLineAlignment": ((2011, LCID, 4, 0),()),
		"FarEastLineBreakControl": ((2012, LCID, 4, 0),()),
		"HangingPunctuation": ((2014, LCID, 4, 0),()),
		"LineRuleAfter": ((2006, LCID, 4, 0),()),
		"LineRuleBefore": ((2005, LCID, 4, 0),()),
		"LineRuleWithin": ((2007, LCID, 4, 0),()),
		"SpaceAfter": ((2009, LCID, 4, 0),()),
		"SpaceBefore": ((2008, LCID, 4, 0),()),
		"SpaceWithin": ((2010, LCID, 4, 0),()),
		"TextDirection": ((2015, LCID, 4, 0),()),
		"WordWrap": ((2013, LCID, 4, 0),()),
	}

class PictureFormat(DispatchBaseClass):
	CLSID = IID('{9149347D-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def IncrementBrightness(self, Increment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((4, 1),),Increment
			)

	def IncrementContrast(self, Increment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((4, 1),),Increment
			)

	_prop_map_get_ = {
		"Application": (2001, 2, (9, 0), (), "Application", None),
		"Brightness": (100, 2, (4, 0), (), "Brightness", None),
		"ColorType": (101, 2, (3, 0), (), "ColorType", None),
		"Contrast": (102, 2, (4, 0), (), "Contrast", None),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		"CropBottom": (103, 2, (4, 0), (), "CropBottom", None),
		"CropLeft": (104, 2, (4, 0), (), "CropLeft", None),
		"CropRight": (105, 2, (4, 0), (), "CropRight", None),
		"CropTop": (106, 2, (4, 0), (), "CropTop", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		"TransparencyColor": (107, 2, (3, 0), (), "TransparencyColor", None),
		"TransparentBackground": (108, 2, (3, 0), (), "TransparentBackground", None),
	}
	_prop_map_put_ = {
		"Brightness": ((100, LCID, 4, 0),()),
		"ColorType": ((101, LCID, 4, 0),()),
		"Contrast": ((102, LCID, 4, 0),()),
		"CropBottom": ((103, LCID, 4, 0),()),
		"CropLeft": ((104, LCID, 4, 0),()),
		"CropRight": ((105, LCID, 4, 0),()),
		"CropTop": ((106, LCID, 4, 0),()),
		"TransparencyColor": ((107, LCID, 4, 0),()),
		"TransparentBackground": ((108, LCID, 4, 0),()),
	}

class PlaceholderFormat(DispatchBaseClass):
	CLSID = IID('{91493477-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Type": (2003, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
	}

class Placeholders(DispatchBaseClass):
	CLSID = IID('{91493476-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type Shape
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{91493479-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{91493479-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class PlaySettings(DispatchBaseClass):
	CLSID = IID('{9149348E-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		"ActionVerb": (2003, 2, (8, 0), (), "ActionVerb", None),
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"HideWhileNotPlaying": (2004, 2, (3, 0), (), "HideWhileNotPlaying", None),
		"LoopUntilStopped": (2005, 2, (3, 0), (), "LoopUntilStopped", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"PauseAnimation": (2008, 2, (3, 0), (), "PauseAnimation", None),
		"PlayOnEntry": (2006, 2, (3, 0), (), "PlayOnEntry", None),
		"RewindMovie": (2007, 2, (3, 0), (), "RewindMovie", None),
		"StopAfterSlides": (2009, 2, (3, 0), (), "StopAfterSlides", None),
	}
	_prop_map_put_ = {
		"ActionVerb": ((2003, LCID, 4, 0),()),
		"HideWhileNotPlaying": ((2004, LCID, 4, 0),()),
		"LoopUntilStopped": ((2005, LCID, 4, 0),()),
		"PauseAnimation": ((2008, LCID, 4, 0),()),
		"PlayOnEntry": ((2006, LCID, 4, 0),()),
		"RewindMovie": ((2007, LCID, 4, 0),()),
		"StopAfterSlides": ((2009, LCID, 4, 0),()),
	}

class Presentations(DispatchBaseClass):
	CLSID = IID('{91493462-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type Presentation
	def Add(self, WithWindow=-1):
		ret = self._oleobj_.InvokeTypes(2003, LCID, 1, (13, 0), ((3, 49),),WithWindow
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(global_IID_IDispatch)
			except global_error:
				return ret
			ret = Dispatch(ret, 'Add', '{91493444-5A91-11CF-8700-00AA0060263B}')
		return ret

	def CanCheckOut(self, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2007, LCID, 1, (11, 0), ((8, 1),),FileName
			)

	def CheckOut(self, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2006, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	# Result is of type Presentation
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (13, 0), ((12, 1),),Index
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(global_IID_IDispatch)
			except global_error:
				return ret
			ret = Dispatch(ret, 'Item', '{91493444-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Presentation
	def Open(self, FileName=defaultNamedNotOptArg, ReadOnly=0, Untitled=0, WithWindow=-1):
		ret = self._oleobj_.InvokeTypes(2005, LCID, 1, (13, 0), ((8, 1), (3, 49), (3, 49), (3, 49)),FileName
			, ReadOnly, Untitled, WithWindow)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(global_IID_IDispatch)
			except global_error:
				return ret
			ret = Dispatch(ret, 'Open', '{91493444-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Presentation
	def OpenOld(self, FileName=defaultNamedNotOptArg, ReadOnly=0, Untitled=0, WithWindow=-1):
		ret = self._oleobj_.InvokeTypes(2004, LCID, 1, (13, 0), ((8, 1), (3, 49), (3, 49), (3, 49)),FileName
			, ReadOnly, Untitled, WithWindow)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(global_IID_IDispatch)
			except global_error:
				return ret
			ret = Dispatch(ret, 'OpenOld', '{91493444-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (13, 0), ((12, 1),),Index
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(global_IID_IDispatch)
			except global_error:
				return ret
			ret = Dispatch(ret, '__call__', '{91493444-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{91493444-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{91493444-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class PrintOptions(DispatchBaseClass):
	CLSID = IID('{9149345D-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		"ActivePrinter": (2015, 2, (8, 0), (), "ActivePrinter", None),
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Collate": (2003, 2, (3, 0), (), "Collate", None),
		"FitToPage": (2004, 2, (3, 0), (), "FitToPage", None),
		"FrameSlides": (2005, 2, (3, 0), (), "FrameSlides", None),
		"HandoutOrder": (2016, 2, (3, 0), (), "HandoutOrder", None),
		"NumberOfCopies": (2006, 2, (3, 0), (), "NumberOfCopies", None),
		"OutputType": (2007, 2, (3, 0), (), "OutputType", None),
		"Parent": (2008, 2, (9, 0), (), "Parent", None),
		"PrintColorType": (2002, 2, (3, 0), (), "PrintColorType", None),
		"PrintComments": (2017, 2, (3, 0), (), "PrintComments", None),
		"PrintFontsAsGraphics": (2013, 2, (3, 0), (), "PrintFontsAsGraphics", None),
		"PrintHiddenSlides": (2009, 2, (3, 0), (), "PrintHiddenSlides", None),
		"PrintInBackground": (2010, 2, (3, 0), (), "PrintInBackground", None),
		"RangeType": (2011, 2, (3, 0), (), "RangeType", None),
		# Method 'Ranges' returns object of type 'PrintRanges'
		"Ranges": (2012, 2, (9, 0), (), "Ranges", '{9149345E-5A91-11CF-8700-00AA0060263B}'),
		"SlideShowName": (2014, 2, (8, 0), (), "SlideShowName", None),
	}
	_prop_map_put_ = {
		"ActivePrinter": ((2015, LCID, 4, 0),()),
		"Collate": ((2003, LCID, 4, 0),()),
		"FitToPage": ((2004, LCID, 4, 0),()),
		"FrameSlides": ((2005, LCID, 4, 0),()),
		"HandoutOrder": ((2016, LCID, 4, 0),()),
		"NumberOfCopies": ((2006, LCID, 4, 0),()),
		"OutputType": ((2007, LCID, 4, 0),()),
		"PrintColorType": ((2002, LCID, 4, 0),()),
		"PrintComments": ((2017, LCID, 4, 0),()),
		"PrintFontsAsGraphics": ((2013, LCID, 4, 0),()),
		"PrintHiddenSlides": ((2009, LCID, 4, 0),()),
		"PrintInBackground": ((2010, LCID, 4, 0),()),
		"RangeType": ((2011, LCID, 4, 0),()),
		"SlideShowName": ((2014, LCID, 4, 0),()),
	}

class PrintRange(DispatchBaseClass):
	CLSID = IID('{9149345F-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Delete(self):
		return self._oleobj_.InvokeTypes(2005, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"End": (2004, 2, (3, 0), (), "End", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Start": (2003, 2, (3, 0), (), "Start", None),
	}
	_prop_map_put_ = {
	}

class PrintRanges(DispatchBaseClass):
	CLSID = IID('{9149345E-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type PrintRange
	def Add(self, Start=defaultNamedNotOptArg, End=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(2001, LCID, 1, (9, 0), ((3, 1), (3, 1)),Start
			, End)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{9149345F-5A91-11CF-8700-00AA0060263B}')
		return ret

	def ClearAll(self):
		return self._oleobj_.InvokeTypes(2003, LCID, 1, (24, 0), (),)

	# Result is of type PrintRange
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{9149345F-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2002, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2004, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{9149345F-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{9149345F-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{9149345F-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class PropertyEffect(DispatchBaseClass):
	CLSID = IID('{914934E9-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"From": (2005, 2, (12, 0), (), "From", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		# Method 'Points' returns object of type 'AnimationPoints'
		"Points": (2004, 2, (9, 0), (), "Points", '{914934EA-5A91-11CF-8700-00AA0060263B}'),
		"Property": (2003, 2, (3, 0), (), "Property", None),
		"To": (2006, 2, (12, 0), (), "To", None),
	}
	_prop_map_put_ = {
		"From": ((2005, LCID, 4, 0),()),
		"Property": ((2003, LCID, 4, 0),()),
		"To": ((2006, LCID, 4, 0),()),
	}

class PublishObject(DispatchBaseClass):
	CLSID = IID('{914934D0-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Publish(self):
		return self._oleobj_.InvokeTypes(2010, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"FileName": (2009, 2, (8, 0), (), "FileName", None),
		"HTMLVersion": (2003, 2, (3, 0), (), "HTMLVersion", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"RangeEnd": (2006, 2, (3, 0), (), "RangeEnd", None),
		"RangeStart": (2005, 2, (3, 0), (), "RangeStart", None),
		"SlideShowName": (2007, 2, (8, 0), (), "SlideShowName", None),
		"SourceType": (2004, 2, (3, 0), (), "SourceType", None),
		"SpeakerNotes": (2008, 2, (3, 0), (), "SpeakerNotes", None),
	}
	_prop_map_put_ = {
		"FileName": ((2009, LCID, 4, 0),()),
		"HTMLVersion": ((2003, LCID, 4, 0),()),
		"RangeEnd": ((2006, LCID, 4, 0),()),
		"RangeStart": ((2005, LCID, 4, 0),()),
		"SlideShowName": ((2007, LCID, 4, 0),()),
		"SourceType": ((2004, LCID, 4, 0),()),
		"SpeakerNotes": ((2008, LCID, 4, 0),()),
	}

class PublishObjects(DispatchBaseClass):
	CLSID = IID('{914934CF-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type PublishObject
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{914934D0-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{914934D0-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{914934D0-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{914934D0-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class RGBColor(DispatchBaseClass):
	CLSID = IID('{91493470-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"RGB": (0, 2, (3, 0), (), "RGB", None),
	}
	_prop_map_put_ = {
		"RGB": ((0, LCID, 4, 0),()),
	}
	# Default property for this class is 'RGB'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (3, 0), (), "RGB", None))
	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class RotationEffect(DispatchBaseClass):
	CLSID = IID('{914934E8-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"By": (2003, 2, (4, 0), (), "By", None),
		"From": (2004, 2, (4, 0), (), "From", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"To": (2005, 2, (4, 0), (), "To", None),
	}
	_prop_map_put_ = {
		"By": ((2003, LCID, 4, 0),()),
		"From": ((2004, LCID, 4, 0),()),
		"To": ((2005, LCID, 4, 0),()),
	}

class Row(DispatchBaseClass):
	CLSID = IID('{914934C7-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Delete(self):
		return self._oleobj_.InvokeTypes(2005, LCID, 1, (24, 0), (),)

	def Select(self):
		return self._oleobj_.InvokeTypes(2004, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Cells' returns object of type 'CellRange'
		"Cells": (2003, 2, (9, 0), (), "Cells", '{914934C8-5A91-11CF-8700-00AA0060263B}'),
		"Height": (2006, 2, (4, 0), (), "Height", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"Height": ((2006, LCID, 4, 0),()),
	}

class Rows(DispatchBaseClass):
	CLSID = IID('{914934C6-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type Row
	def Add(self, BeforeRow=-1):
		ret = self._oleobj_.InvokeTypes(2003, LCID, 1, (9, 0), ((3, 49),),BeforeRow
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{914934C7-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Row
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{914934C7-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{914934C7-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{914934C7-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{914934C7-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class Ruler(DispatchBaseClass):
	CLSID = IID('{91493490-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Levels' returns object of type 'RulerLevels'
		"Levels": (2004, 2, (9, 0), (), "Levels", '{91493491-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		# Method 'TabStops' returns object of type 'TabStops'
		"TabStops": (2003, 2, (9, 0), (), "TabStops", '{91493493-5A91-11CF-8700-00AA0060263B}'),
	}
	_prop_map_put_ = {
	}

class RulerLevel(DispatchBaseClass):
	CLSID = IID('{91493492-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"FirstMargin": (2003, 2, (4, 0), (), "FirstMargin", None),
		"LeftMargin": (2004, 2, (4, 0), (), "LeftMargin", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"FirstMargin": ((2003, LCID, 4, 0),()),
		"LeftMargin": ((2004, LCID, 4, 0),()),
	}

class RulerLevels(DispatchBaseClass):
	CLSID = IID('{91493491-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type RulerLevel
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{91493492-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{91493492-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{91493492-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{91493492-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class ScaleEffect(DispatchBaseClass):
	CLSID = IID('{914934E7-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"ByX": (2003, 2, (4, 0), (), "ByX", None),
		"ByY": (2004, 2, (4, 0), (), "ByY", None),
		"FromX": (2005, 2, (4, 0), (), "FromX", None),
		"FromY": (2006, 2, (4, 0), (), "FromY", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"ToX": (2007, 2, (4, 0), (), "ToX", None),
		"ToY": (2008, 2, (4, 0), (), "ToY", None),
	}
	_prop_map_put_ = {
		"ByX": ((2003, LCID, 4, 0),()),
		"ByY": ((2004, LCID, 4, 0),()),
		"FromX": ((2005, LCID, 4, 0),()),
		"FromY": ((2006, LCID, 4, 0),()),
		"ToX": ((2007, LCID, 4, 0),()),
		"ToY": ((2008, LCID, 4, 0),()),
	}

class Selection(DispatchBaseClass):
	CLSID = IID('{91493454-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Copy(self):
		return self._oleobj_.InvokeTypes(2004, LCID, 1, (24, 0), (),)

	def Cut(self):
		return self._oleobj_.InvokeTypes(2003, LCID, 1, (24, 0), (),)

	def Delete(self):
		return self._oleobj_.InvokeTypes(2005, LCID, 1, (24, 0), (),)

	def Unselect(self):
		return self._oleobj_.InvokeTypes(2006, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		# Method 'ChildShapeRange' returns object of type 'ShapeRange'
		"ChildShapeRange": (2011, 2, (9, 0), (), "ChildShapeRange", '{9149347A-5A91-11CF-8700-00AA0060263B}'),
		"HasChildShapeRange": (2012, 2, (11, 0), (), "HasChildShapeRange", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		# Method 'ShapeRange' returns object of type 'ShapeRange'
		"ShapeRange": (2009, 2, (9, 0), (), "ShapeRange", '{9149347A-5A91-11CF-8700-00AA0060263B}'),
		# Method 'SlideRange' returns object of type 'SlideRange'
		"SlideRange": (2008, 2, (9, 0), (), "SlideRange", '{9149346B-5A91-11CF-8700-00AA0060263B}'),
		# Method 'TextRange' returns object of type 'TextRange'
		"TextRange": (2010, 2, (9, 0), (), "TextRange", '{9149348F-5A91-11CF-8700-00AA0060263B}'),
		"Type": (2007, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
	}

class Sequence(DispatchBaseClass):
	CLSID = IID('{914934DE-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type Effect
	def AddEffect(self, Shape=defaultNamedNotOptArg, effectId=defaultNamedNotOptArg, Level=0, trigger=1
			, Index=-1):
		ret = self._oleobj_.InvokeTypes(2003, LCID, 1, (9, 0), ((9, 1), (3, 1), (3, 49), (3, 49), (3, 49)),Shape
			, effectId, Level, trigger, Index)
		if ret is not None:
			ret = Dispatch(ret, 'AddEffect', '{914934DF-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Effect
	def Clone(self, Effect=defaultNamedNotOptArg, Index=-1):
		ret = self._oleobj_.InvokeTypes(2004, LCID, 1, (9, 0), ((9, 1), (3, 49)),Effect
			, Index)
		if ret is not None:
			ret = Dispatch(ret, 'Clone', '{914934DF-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Effect
	def ConvertToAfterEffect(self, Effect=defaultNamedNotOptArg, After=defaultNamedNotOptArg, DimColor=0, DimSchemeColor=0):
		ret = self._oleobj_.InvokeTypes(2008, LCID, 1, (9, 0), ((9, 1), (3, 1), (3, 49), (3, 49)),Effect
			, After, DimColor, DimSchemeColor)
		if ret is not None:
			ret = Dispatch(ret, 'ConvertToAfterEffect', '{914934DF-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Effect
	def ConvertToAnimateBackground(self, Effect=defaultNamedNotOptArg, AnimateBackground=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(2009, LCID, 1, (9, 0), ((9, 1), (3, 1)),Effect
			, AnimateBackground)
		if ret is not None:
			ret = Dispatch(ret, 'ConvertToAnimateBackground', '{914934DF-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Effect
	def ConvertToAnimateInReverse(self, Effect=defaultNamedNotOptArg, animateInReverse=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(2010, LCID, 1, (9, 0), ((9, 1), (3, 1)),Effect
			, animateInReverse)
		if ret is not None:
			ret = Dispatch(ret, 'ConvertToAnimateInReverse', '{914934DF-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Effect
	def ConvertToBuildLevel(self, Effect=defaultNamedNotOptArg, Level=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(2007, LCID, 1, (9, 0), ((9, 1), (3, 1)),Effect
			, Level)
		if ret is not None:
			ret = Dispatch(ret, 'ConvertToBuildLevel', '{914934DF-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Effect
	def ConvertToTextUnitEffect(self, Effect=defaultNamedNotOptArg, unitEffect=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(2011, LCID, 1, (9, 0), ((9, 1), (3, 1)),Effect
			, unitEffect)
		if ret is not None:
			ret = Dispatch(ret, 'ConvertToTextUnitEffect', '{914934DF-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Effect
	def FindFirstAnimationFor(self, Shape=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(2005, LCID, 1, (9, 0), ((9, 1),),Shape
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindFirstAnimationFor', '{914934DF-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Effect
	def FindFirstAnimationForClick(self, click=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(2006, LCID, 1, (9, 0), ((3, 1),),click
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindFirstAnimationForClick', '{914934DF-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Effect
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{914934DF-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{914934DF-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{914934DF-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{914934DF-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class Sequences(DispatchBaseClass):
	CLSID = IID('{914934DD-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type Sequence
	def Add(self, Index=-1):
		ret = self._oleobj_.InvokeTypes(2003, LCID, 1, (9, 0), ((3, 49),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{914934DE-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Sequence
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{914934DE-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{914934DE-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{914934DE-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{914934DE-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class SetEffect(DispatchBaseClass):
	CLSID = IID('{914934F1-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Property": (2003, 2, (3, 0), (), "Property", None),
		"To": (2004, 2, (12, 0), (), "To", None),
	}
	_prop_map_put_ = {
		"Property": ((2003, LCID, 4, 0),()),
		"To": ((2004, LCID, 4, 0),()),
	}

class ShadowFormat(DispatchBaseClass):
	CLSID = IID('{91493480-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def IncrementOffsetX(self, Increment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((4, 1),),Increment
			)

	def IncrementOffsetY(self, Increment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((4, 1),),Increment
			)

	_prop_map_get_ = {
		"Application": (2001, 2, (9, 0), (), "Application", None),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		# Method 'ForeColor' returns object of type 'ColorFormat'
		"ForeColor": (100, 2, (9, 0), (), "ForeColor", '{91493452-5A91-11CF-8700-00AA0060263B}'),
		"Obscured": (101, 2, (3, 0), (), "Obscured", None),
		"OffsetX": (102, 2, (4, 0), (), "OffsetX", None),
		"OffsetY": (103, 2, (4, 0), (), "OffsetY", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		"Transparency": (104, 2, (4, 0), (), "Transparency", None),
		"Type": (105, 2, (3, 0), (), "Type", None),
		"Visible": (106, 2, (3, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"ForeColor": ((100, LCID, 4, 0),()),
		"Obscured": ((101, LCID, 4, 0),()),
		"OffsetX": ((102, LCID, 4, 0),()),
		"OffsetY": ((103, LCID, 4, 0),()),
		"Transparency": ((104, LCID, 4, 0),()),
		"Type": ((105, LCID, 4, 0),()),
		"Visible": ((106, LCID, 4, 0),()),
	}

class Shape(DispatchBaseClass):
	CLSID = IID('{91493479-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Apply(self):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), (),)

	def CanvasCropBottom(self, Increment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(143, LCID, 1, (24, 0), ((4, 1),),Increment
			)

	def CanvasCropLeft(self, Increment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(140, LCID, 1, (24, 0), ((4, 1),),Increment
			)

	def CanvasCropRight(self, Increment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(142, LCID, 1, (24, 0), ((4, 1),),Increment
			)

	def CanvasCropTop(self, Increment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(141, LCID, 1, (24, 0), ((4, 1),),Increment
			)

	def Copy(self):
		return self._oleobj_.InvokeTypes(2010, LCID, 1, (24, 0), (),)

	def Cut(self):
		return self._oleobj_.InvokeTypes(2009, LCID, 1, (24, 0), (),)

	def Delete(self):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	# Result is of type ShapeRange
	def Duplicate(self):
		ret = self._oleobj_.InvokeTypes(2012, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', '{9149347A-5A91-11CF-8700-00AA0060263B}')
		return ret

	def Export(self, PathName=defaultNamedNotOptArg, Filter=defaultNamedNotOptArg, ScaleWidth=0, ScaleHeight=0
			, ExportMode=1):
		return self._oleobj_.InvokeTypes(2018, LCID, 1, (24, 0), ((8, 1), (3, 1), (3, 49), (3, 49), (3, 49)),PathName
			, Filter, ScaleWidth, ScaleHeight, ExportMode)

	def Flip(self, FlipCmd=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((3, 1),),FlipCmd
			)

	def IncrementLeft(self, Increment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((4, 1),),Increment
			)

	def IncrementRotation(self, Increment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), ((4, 1),),Increment
			)

	def IncrementTop(self, Increment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((4, 1),),Increment
			)

	def PickUp(self):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), (),)

	def RerouteConnections(self):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), (),)

	def ScaleHeight(self, Factor=defaultNamedNotOptArg, RelativeToOriginalSize=defaultNamedNotOptArg, fScale=0):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), ((4, 1), (3, 1), (3, 49)),Factor
			, RelativeToOriginalSize, fScale)

	def ScaleWidth(self, Factor=defaultNamedNotOptArg, RelativeToOriginalSize=defaultNamedNotOptArg, fScale=0):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), ((4, 1), (3, 1), (3, 49)),Factor
			, RelativeToOriginalSize, fScale)

	def Select(self, Replace=-1):
		return self._oleobj_.InvokeTypes(2011, LCID, 1, (24, 0), ((3, 49),),Replace
			)

	def SetShapesDefaultProperties(self):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	# Result is of type ShapeRange
	def Ungroup(self):
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Ungroup', '{9149347A-5A91-11CF-8700-00AA0060263B}')
		return ret

	def ZOrder(self, ZOrderCmd=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(24, LCID, 1, (24, 0), ((3, 1),),ZOrderCmd
			)

	_prop_map_get_ = {
		# Method 'ActionSettings' returns object of type 'ActionSettings'
		"ActionSettings": (2007, 2, (9, 0), (), "ActionSettings", '{9149348C-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Adjustments' returns object of type 'Adjustments'
		"Adjustments": (100, 2, (9, 0), (), "Adjustments", '{9149347C-5A91-11CF-8700-00AA0060263B}'),
		"AlternativeText": (131, 2, (8, 0), (), "AlternativeText", None),
		# Method 'AnimationSettings' returns object of type 'AnimationSettings'
		"AnimationSettings": (2006, 2, (9, 0), (), "AnimationSettings", '{9149348B-5A91-11CF-8700-00AA0060263B}'),
		"Application": (2001, 2, (9, 0), (), "Application", None),
		"AutoShapeType": (101, 2, (3, 0), (), "AutoShapeType", None),
		"BlackWhiteMode": (102, 2, (3, 0), (), "BlackWhiteMode", None),
		# Method 'Callout' returns object of type 'CalloutFormat'
		"Callout": (103, 2, (9, 0), (), "Callout", '{91493485-5A91-11CF-8700-00AA0060263B}'),
		# Method 'CanvasItems' returns object of type 'CanvasShapes'
		"CanvasItems": (138, 2, (9, 0), (), "CanvasItems", '{914934EC-5A91-11CF-8700-00AA0060263B}'),
		"Child": (136, 2, (3, 0), (), "Child", None),
		"ConnectionSiteCount": (104, 2, (3, 0), (), "ConnectionSiteCount", None),
		"Connector": (105, 2, (3, 0), (), "Connector", None),
		# Method 'ConnectorFormat' returns object of type 'ConnectorFormat'
		"ConnectorFormat": (106, 2, (9, 0), (), "ConnectorFormat", '{91493481-5A91-11CF-8700-00AA0060263B}'),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		# Method 'Diagram' returns object of type 'Diagram'
		"Diagram": (133, 2, (9, 0), (), "Diagram", '{914934DB-5A91-11CF-8700-00AA0060263B}'),
		# Method 'DiagramNode' returns object of type 'DiagramNode'
		"DiagramNode": (135, 2, (9, 0), (), "DiagramNode", '{914934D8-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Fill' returns object of type 'FillFormat'
		"Fill": (107, 2, (9, 0), (), "Fill", '{9149347E-5A91-11CF-8700-00AA0060263B}'),
		# Method 'GroupItems' returns object of type 'GroupShapes'
		"GroupItems": (108, 2, (9, 0), (), "GroupItems", '{9149347B-5A91-11CF-8700-00AA0060263B}'),
		"HasDiagram": (132, 2, (3, 0), (), "HasDiagram", None),
		"HasDiagramNode": (134, 2, (3, 0), (), "HasDiagramNode", None),
		"HasTable": (2016, 2, (3, 0), (), "HasTable", None),
		"HasTextFrame": (2014, 2, (3, 0), (), "HasTextFrame", None),
		"Height": (109, 2, (4, 0), (), "Height", None),
		"HorizontalFlip": (110, 2, (3, 0), (), "HorizontalFlip", None),
		"Id": (139, 2, (3, 0), (), "Id", None),
		"Left": (111, 2, (4, 0), (), "Left", None),
		# Method 'Line' returns object of type 'LineFormat'
		"Line": (112, 2, (9, 0), (), "Line", '{9149347F-5A91-11CF-8700-00AA0060263B}'),
		# Method 'LinkFormat' returns object of type 'LinkFormat'
		"LinkFormat": (2004, 2, (9, 0), (), "LinkFormat", '{91493489-5A91-11CF-8700-00AA0060263B}'),
		"LockAspectRatio": (113, 2, (3, 0), (), "LockAspectRatio", None),
		"MediaType": (2013, 2, (3, 0), (), "MediaType", None),
		"Name": (115, 2, (8, 0), (), "Name", None),
		# Method 'Nodes' returns object of type 'ShapeNodes'
		"Nodes": (116, 2, (9, 0), (), "Nodes", '{91493486-5A91-11CF-8700-00AA0060263B}'),
		# Method 'OLEFormat' returns object of type 'OLEFormat'
		"OLEFormat": (2003, 2, (9, 0), (), "OLEFormat", '{91493488-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'ParentGroup' returns object of type 'Shape'
		"ParentGroup": (137, 2, (9, 0), (), "ParentGroup", '{91493479-5A91-11CF-8700-00AA0060263B}'),
		# Method 'PictureFormat' returns object of type 'PictureFormat'
		"PictureFormat": (118, 2, (9, 0), (), "PictureFormat", '{9149347D-5A91-11CF-8700-00AA0060263B}'),
		# Method 'PlaceholderFormat' returns object of type 'PlaceholderFormat'
		"PlaceholderFormat": (2005, 2, (9, 0), (), "PlaceholderFormat", '{91493477-5A91-11CF-8700-00AA0060263B}'),
		"Rotation": (117, 2, (4, 0), (), "Rotation", None),
		# Method 'Script' returns object of type 'Script'
		"Script": (130, 2, (9, 0), (), "Script", '{000C0341-0000-0000-C000-000000000046}'),
		# Method 'Shadow' returns object of type 'ShadowFormat'
		"Shadow": (119, 2, (9, 0), (), "Shadow", '{91493480-5A91-11CF-8700-00AA0060263B}'),
		# Method 'SoundFormat' returns object of type 'SoundFormat'
		"SoundFormat": (2015, 2, (9, 0), (), "SoundFormat", '{91493473-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Table' returns object of type 'Table'
		"Table": (2017, 2, (9, 0), (), "Table", '{914934C3-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Tags' returns object of type 'Tags'
		"Tags": (2008, 2, (9, 0), (), "Tags", '{914934B9-5A91-11CF-8700-00AA0060263B}'),
		# Method 'TextEffect' returns object of type 'TextEffectFormat'
		"TextEffect": (120, 2, (9, 0), (), "TextEffect", '{91493482-5A91-11CF-8700-00AA0060263B}'),
		# Method 'TextFrame' returns object of type 'TextFrame'
		"TextFrame": (121, 2, (9, 0), (), "TextFrame", '{91493484-5A91-11CF-8700-00AA0060263B}'),
		# Method 'ThreeD' returns object of type 'ThreeDFormat'
		"ThreeD": (122, 2, (9, 0), (), "ThreeD", '{91493483-5A91-11CF-8700-00AA0060263B}'),
		"Top": (123, 2, (4, 0), (), "Top", None),
		"Type": (124, 2, (3, 0), (), "Type", None),
		"VerticalFlip": (125, 2, (3, 0), (), "VerticalFlip", None),
		"Vertices": (126, 2, (12, 0), (), "Vertices", None),
		"Visible": (127, 2, (3, 0), (), "Visible", None),
		"Width": (128, 2, (4, 0), (), "Width", None),
		"ZOrderPosition": (129, 2, (3, 0), (), "ZOrderPosition", None),
	}
	_prop_map_put_ = {
		"AlternativeText": ((131, LCID, 4, 0),()),
		"AutoShapeType": ((101, LCID, 4, 0),()),
		"BlackWhiteMode": ((102, LCID, 4, 0),()),
		"Height": ((109, LCID, 4, 0),()),
		"Left": ((111, LCID, 4, 0),()),
		"LockAspectRatio": ((113, LCID, 4, 0),()),
		"Name": ((115, LCID, 4, 0),()),
		"RTF": ((144, LCID, 4, 0),()),
		"Rotation": ((117, LCID, 4, 0),()),
		"Top": ((123, LCID, 4, 0),()),
		"Visible": ((127, LCID, 4, 0),()),
		"Width": ((128, LCID, 4, 0),()),
	}

class ShapeNode(DispatchBaseClass):
	CLSID = IID('{91493487-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Application": (2001, 2, (9, 0), (), "Application", None),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		"EditingType": (100, 2, (3, 0), (), "EditingType", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		"Points": (101, 2, (12, 0), (), "Points", None),
		"SegmentType": (102, 2, (3, 0), (), "SegmentType", None),
	}
	_prop_map_put_ = {
	}

class ShapeNodes(DispatchBaseClass):
	CLSID = IID('{91493486-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Delete(self, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((3, 1),),Index
			)

	def Insert(self, Index=defaultNamedNotOptArg, SegmentType=defaultNamedNotOptArg, EditingType=defaultNamedNotOptArg, X1=defaultNamedNotOptArg
			, Y1=defaultNamedNotOptArg, X2=0.0, Y2=0.0, X3=0.0, Y3=0.0):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (4, 1), (4, 1), (4, 49), (4, 49), (4, 49), (4, 49)),Index
			, SegmentType, EditingType, X1, Y1, X2
			, Y2, X3, Y3)

	# Result is of type ShapeNode
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{91493487-5A91-11CF-8700-00AA0060263B}')
		return ret

	def SetEditingType(self, Index=defaultNamedNotOptArg, EditingType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((3, 1), (3, 1)),Index
			, EditingType)

	def SetPosition(self, Index=defaultNamedNotOptArg, X1=defaultNamedNotOptArg, Y1=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((3, 1), (4, 1), (4, 1)),Index
			, X1, Y1)

	def SetSegmentType(self, Index=defaultNamedNotOptArg, SegmentType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), ((3, 1), (3, 1)),Index
			, SegmentType)

	_prop_map_get_ = {
		"Application": (2001, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{91493487-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{91493487-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{91493487-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class ShapeRange(DispatchBaseClass):
	CLSID = IID('{9149347A-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Align(self, AlignCmd=defaultNamedNotOptArg, RelativeTo=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2018, LCID, 1, (24, 0), ((3, 1), (3, 1)),AlignCmd
			, RelativeTo)

	def Apply(self):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), (),)

	def CanvasCropBottom(self, Increment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(143, LCID, 1, (24, 0), ((4, 1),),Increment
			)

	def CanvasCropLeft(self, Increment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(140, LCID, 1, (24, 0), ((4, 1),),Increment
			)

	def CanvasCropRight(self, Increment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(142, LCID, 1, (24, 0), ((4, 1),),Increment
			)

	def CanvasCropTop(self, Increment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(141, LCID, 1, (24, 0), ((4, 1),),Increment
			)

	def Copy(self):
		return self._oleobj_.InvokeTypes(2010, LCID, 1, (24, 0), (),)

	def Cut(self):
		return self._oleobj_.InvokeTypes(2009, LCID, 1, (24, 0), (),)

	def Delete(self):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	def Distribute(self, DistributeCmd=defaultNamedNotOptArg, RelativeTo=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2019, LCID, 1, (24, 0), ((3, 1), (3, 1)),DistributeCmd
			, RelativeTo)

	# Result is of type ShapeRange
	def Duplicate(self):
		ret = self._oleobj_.InvokeTypes(2012, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', '{9149347A-5A91-11CF-8700-00AA0060263B}')
		return ret

	def Export(self, PathName=defaultNamedNotOptArg, Filter=defaultNamedNotOptArg, ScaleWidth=0, ScaleHeight=0
			, ExportMode=1):
		return self._oleobj_.InvokeTypes(2023, LCID, 1, (24, 0), ((8, 1), (3, 1), (3, 49), (3, 49), (3, 49)),PathName
			, Filter, ScaleWidth, ScaleHeight, ExportMode)

	def Flip(self, FlipCmd=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((3, 1),),FlipCmd
			)

	# Result is of type Shape
	def Group(self):
		ret = self._oleobj_.InvokeTypes(2016, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Group', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	def IncrementLeft(self, Increment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((4, 1),),Increment
			)

	def IncrementRotation(self, Increment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), ((4, 1),),Increment
			)

	def IncrementTop(self, Increment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((4, 1),),Increment
			)

	# Result is of type Shape
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	def PickUp(self):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), (),)

	# Result is of type Shape
	def Regroup(self):
		ret = self._oleobj_.InvokeTypes(2017, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Regroup', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	def RerouteConnections(self):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), (),)

	def ScaleHeight(self, Factor=defaultNamedNotOptArg, RelativeToOriginalSize=defaultNamedNotOptArg, fScale=0):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), ((4, 1), (3, 1), (3, 49)),Factor
			, RelativeToOriginalSize, fScale)

	def ScaleWidth(self, Factor=defaultNamedNotOptArg, RelativeToOriginalSize=defaultNamedNotOptArg, fScale=0):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), ((4, 1), (3, 1), (3, 49)),Factor
			, RelativeToOriginalSize, fScale)

	def Select(self, Replace=-1):
		return self._oleobj_.InvokeTypes(2011, LCID, 1, (24, 0), ((3, 49),),Replace
			)

	def SetShapesDefaultProperties(self):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	# Result is of type ShapeRange
	def Ungroup(self):
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Ungroup', '{9149347A-5A91-11CF-8700-00AA0060263B}')
		return ret

	def ZOrder(self, ZOrderCmd=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(24, LCID, 1, (24, 0), ((3, 1),),ZOrderCmd
			)

	_prop_map_get_ = {
		# Method 'ActionSettings' returns object of type 'ActionSettings'
		"ActionSettings": (2007, 2, (9, 0), (), "ActionSettings", '{9149348C-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Adjustments' returns object of type 'Adjustments'
		"Adjustments": (100, 2, (9, 0), (), "Adjustments", '{9149347C-5A91-11CF-8700-00AA0060263B}'),
		"AlternativeText": (131, 2, (8, 0), (), "AlternativeText", None),
		# Method 'AnimationSettings' returns object of type 'AnimationSettings'
		"AnimationSettings": (2006, 2, (9, 0), (), "AnimationSettings", '{9149348B-5A91-11CF-8700-00AA0060263B}'),
		"Application": (2001, 2, (9, 0), (), "Application", None),
		"AutoShapeType": (101, 2, (3, 0), (), "AutoShapeType", None),
		"BlackWhiteMode": (102, 2, (3, 0), (), "BlackWhiteMode", None),
		# Method 'Callout' returns object of type 'CalloutFormat'
		"Callout": (103, 2, (9, 0), (), "Callout", '{91493485-5A91-11CF-8700-00AA0060263B}'),
		# Method 'CanvasItems' returns object of type 'CanvasShapes'
		"CanvasItems": (138, 2, (9, 0), (), "CanvasItems", '{914934EC-5A91-11CF-8700-00AA0060263B}'),
		"Child": (136, 2, (3, 0), (), "Child", None),
		"ConnectionSiteCount": (104, 2, (3, 0), (), "ConnectionSiteCount", None),
		"Connector": (105, 2, (3, 0), (), "Connector", None),
		# Method 'ConnectorFormat' returns object of type 'ConnectorFormat'
		"ConnectorFormat": (106, 2, (9, 0), (), "ConnectorFormat", '{91493481-5A91-11CF-8700-00AA0060263B}'),
		"Count": (9, 2, (3, 0), (), "Count", None),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		# Method 'Diagram' returns object of type 'Diagram'
		"Diagram": (133, 2, (9, 0), (), "Diagram", '{914934DB-5A91-11CF-8700-00AA0060263B}'),
		# Method 'DiagramNode' returns object of type 'DiagramNode'
		"DiagramNode": (135, 2, (9, 0), (), "DiagramNode", '{914934D8-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Fill' returns object of type 'FillFormat'
		"Fill": (107, 2, (9, 0), (), "Fill", '{9149347E-5A91-11CF-8700-00AA0060263B}'),
		# Method 'GroupItems' returns object of type 'GroupShapes'
		"GroupItems": (108, 2, (9, 0), (), "GroupItems", '{9149347B-5A91-11CF-8700-00AA0060263B}'),
		"HasDiagram": (132, 2, (3, 0), (), "HasDiagram", None),
		"HasDiagramNode": (134, 2, (3, 0), (), "HasDiagramNode", None),
		"HasTable": (2021, 2, (3, 0), (), "HasTable", None),
		"HasTextFrame": (2014, 2, (3, 0), (), "HasTextFrame", None),
		"Height": (109, 2, (4, 0), (), "Height", None),
		"HorizontalFlip": (110, 2, (3, 0), (), "HorizontalFlip", None),
		"Id": (139, 2, (3, 0), (), "Id", None),
		"Left": (111, 2, (4, 0), (), "Left", None),
		# Method 'Line' returns object of type 'LineFormat'
		"Line": (112, 2, (9, 0), (), "Line", '{9149347F-5A91-11CF-8700-00AA0060263B}'),
		# Method 'LinkFormat' returns object of type 'LinkFormat'
		"LinkFormat": (2004, 2, (9, 0), (), "LinkFormat", '{91493489-5A91-11CF-8700-00AA0060263B}'),
		"LockAspectRatio": (113, 2, (3, 0), (), "LockAspectRatio", None),
		"MediaType": (2013, 2, (3, 0), (), "MediaType", None),
		"Name": (115, 2, (8, 0), (), "Name", None),
		# Method 'Nodes' returns object of type 'ShapeNodes'
		"Nodes": (116, 2, (9, 0), (), "Nodes", '{91493486-5A91-11CF-8700-00AA0060263B}'),
		# Method 'OLEFormat' returns object of type 'OLEFormat'
		"OLEFormat": (2003, 2, (9, 0), (), "OLEFormat", '{91493488-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'ParentGroup' returns object of type 'Shape'
		"ParentGroup": (137, 2, (9, 0), (), "ParentGroup", '{91493479-5A91-11CF-8700-00AA0060263B}'),
		# Method 'PictureFormat' returns object of type 'PictureFormat'
		"PictureFormat": (118, 2, (9, 0), (), "PictureFormat", '{9149347D-5A91-11CF-8700-00AA0060263B}'),
		# Method 'PlaceholderFormat' returns object of type 'PlaceholderFormat'
		"PlaceholderFormat": (2005, 2, (9, 0), (), "PlaceholderFormat", '{91493477-5A91-11CF-8700-00AA0060263B}'),
		"Rotation": (117, 2, (4, 0), (), "Rotation", None),
		# Method 'Script' returns object of type 'Script'
		"Script": (130, 2, (9, 0), (), "Script", '{000C0341-0000-0000-C000-000000000046}'),
		# Method 'Shadow' returns object of type 'ShadowFormat'
		"Shadow": (119, 2, (9, 0), (), "Shadow", '{91493480-5A91-11CF-8700-00AA0060263B}'),
		# Method 'SoundFormat' returns object of type 'SoundFormat'
		"SoundFormat": (2015, 2, (9, 0), (), "SoundFormat", '{91493473-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Table' returns object of type 'Table'
		"Table": (2022, 2, (9, 0), (), "Table", '{914934C3-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Tags' returns object of type 'Tags'
		"Tags": (2008, 2, (9, 0), (), "Tags", '{914934B9-5A91-11CF-8700-00AA0060263B}'),
		# Method 'TextEffect' returns object of type 'TextEffectFormat'
		"TextEffect": (120, 2, (9, 0), (), "TextEffect", '{91493482-5A91-11CF-8700-00AA0060263B}'),
		# Method 'TextFrame' returns object of type 'TextFrame'
		"TextFrame": (121, 2, (9, 0), (), "TextFrame", '{91493484-5A91-11CF-8700-00AA0060263B}'),
		# Method 'ThreeD' returns object of type 'ThreeDFormat'
		"ThreeD": (122, 2, (9, 0), (), "ThreeD", '{91493483-5A91-11CF-8700-00AA0060263B}'),
		"Top": (123, 2, (4, 0), (), "Top", None),
		"Type": (124, 2, (3, 0), (), "Type", None),
		"VerticalFlip": (125, 2, (3, 0), (), "VerticalFlip", None),
		"Vertices": (126, 2, (12, 0), (), "Vertices", None),
		"Visible": (127, 2, (3, 0), (), "Visible", None),
		"Width": (128, 2, (4, 0), (), "Width", None),
		"ZOrderPosition": (129, 2, (3, 0), (), "ZOrderPosition", None),
	}
	_prop_map_put_ = {
		"AlternativeText": ((131, LCID, 4, 0),()),
		"AutoShapeType": ((101, LCID, 4, 0),()),
		"BlackWhiteMode": ((102, LCID, 4, 0),()),
		"Height": ((109, LCID, 4, 0),()),
		"Left": ((111, LCID, 4, 0),()),
		"LockAspectRatio": ((113, LCID, 4, 0),()),
		"Name": ((115, LCID, 4, 0),()),
		"RTF": ((144, LCID, 4, 0),()),
		"Rotation": ((117, LCID, 4, 0),()),
		"Top": ((123, LCID, 4, 0),()),
		"Visible": ((127, LCID, 4, 0),()),
		"Width": ((128, LCID, 4, 0),()),
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{91493479-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{91493479-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(9, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class Shapes(DispatchBaseClass):
	CLSID = IID('{91493475-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type Shape
	def AddCallout(self, Type=defaultNamedNotOptArg, Left=defaultNamedNotOptArg, Top=defaultNamedNotOptArg, Width=defaultNamedNotOptArg
			, Height=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), ((3, 1), (4, 1), (4, 1), (4, 1), (4, 1)),Type
			, Left, Top, Width, Height)
		if ret is not None:
			ret = Dispatch(ret, 'AddCallout', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddCanvas(self, Left=defaultNamedNotOptArg, Top=defaultNamedNotOptArg, Width=defaultNamedNotOptArg, Height=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(25, LCID, 1, (9, 0), ((4, 1), (4, 1), (4, 1), (4, 1)),Left
			, Top, Width, Height)
		if ret is not None:
			ret = Dispatch(ret, 'AddCanvas', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddComment(self, Left=1.25, Top=1.25, Width=145.25, Height=145.25):
		ret = self._oleobj_.InvokeTypes(2009, LCID, 1, (9, 0), ((4, 49), (4, 49), (4, 49), (4, 49)),Left
			, Top, Width, Height)
		if ret is not None:
			ret = Dispatch(ret, 'AddComment', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddConnector(self, Type=defaultNamedNotOptArg, BeginX=defaultNamedNotOptArg, BeginY=defaultNamedNotOptArg, EndX=defaultNamedNotOptArg
			, EndY=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), ((3, 1), (4, 1), (4, 1), (4, 1), (4, 1)),Type
			, BeginX, BeginY, EndX, EndY)
		if ret is not None:
			ret = Dispatch(ret, 'AddConnector', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddCurve(self, SafeArrayOfPoints=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(12, LCID, 1, (9, 0), ((12, 1),),SafeArrayOfPoints
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddCurve', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddDiagram(self, Type=defaultNamedNotOptArg, Left=defaultNamedNotOptArg, Top=defaultNamedNotOptArg, Width=defaultNamedNotOptArg
			, Height=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((3, 1), (4, 1), (4, 1), (4, 1), (4, 1)),Type
			, Left, Top, Width, Height)
		if ret is not None:
			ret = Dispatch(ret, 'AddDiagram', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddLabel(self, Orientation=defaultNamedNotOptArg, Left=defaultNamedNotOptArg, Top=defaultNamedNotOptArg, Width=defaultNamedNotOptArg
			, Height=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), ((3, 1), (4, 1), (4, 1), (4, 1), (4, 1)),Orientation
			, Left, Top, Width, Height)
		if ret is not None:
			ret = Dispatch(ret, 'AddLabel', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddLine(self, BeginX=defaultNamedNotOptArg, BeginY=defaultNamedNotOptArg, EndX=defaultNamedNotOptArg, EndY=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), ((4, 1), (4, 1), (4, 1), (4, 1)),BeginX
			, BeginY, EndX, EndY)
		if ret is not None:
			ret = Dispatch(ret, 'AddLine', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddMediaObject(self, FileName=defaultNamedNotOptArg, Left=0.0, Top=0.0, Width=-1.0
			, Height=-1.0):
		ret = self._oleobj_.InvokeTypes(2011, LCID, 1, (9, 0), ((8, 1), (4, 49), (4, 49), (4, 49), (4, 49)),FileName
			, Left, Top, Width, Height)
		if ret is not None:
			ret = Dispatch(ret, 'AddMediaObject', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddOLEObject(self, Left=0.0, Top=0.0, Width=-1.0, Height=-1.0
			, ClassName='', FileName='', DisplayAsIcon=0, IconFileName='', IconIndex=0
			, IconLabel='', Link=0):
		return self._ApplyTypes_(2008, 1, (9, 32), ((4, 49), (4, 49), (4, 49), (4, 49), (8, 49), (8, 49), (3, 49), (8, 49), (3, 49), (8, 49), (3, 49)), 'AddOLEObject', '{91493479-5A91-11CF-8700-00AA0060263B}',Left
			, Top, Width, Height, ClassName, FileName
			, DisplayAsIcon, IconFileName, IconIndex, IconLabel, Link
			)

	# Result is of type Shape
	def AddPicture(self, FileName=defaultNamedNotOptArg, LinkToFile=defaultNamedNotOptArg, SaveWithDocument=defaultNamedNotOptArg, Left=defaultNamedNotOptArg
			, Top=defaultNamedNotOptArg, Width=-1.0, Height=-1.0):
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), ((8, 1), (3, 1), (3, 1), (4, 1), (4, 1), (4, 49), (4, 49)),FileName
			, LinkToFile, SaveWithDocument, Left, Top, Width
			, Height)
		if ret is not None:
			ret = Dispatch(ret, 'AddPicture', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddPlaceholder(self, Type=defaultNamedNotOptArg, Left=-1.0, Top=-1.0, Width=-1.0
			, Height=-1.0):
		ret = self._oleobj_.InvokeTypes(2010, LCID, 1, (9, 0), ((3, 1), (4, 49), (4, 49), (4, 49), (4, 49)),Type
			, Left, Top, Width, Height)
		if ret is not None:
			ret = Dispatch(ret, 'AddPlaceholder', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddPolyline(self, SafeArrayOfPoints=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(16, LCID, 1, (9, 0), ((12, 1),),SafeArrayOfPoints
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddPolyline', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddShape(self, Type=defaultNamedNotOptArg, Left=defaultNamedNotOptArg, Top=defaultNamedNotOptArg, Width=defaultNamedNotOptArg
			, Height=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), ((3, 1), (4, 1), (4, 1), (4, 1), (4, 1)),Type
			, Left, Top, Width, Height)
		if ret is not None:
			ret = Dispatch(ret, 'AddShape', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddTable(self, NumRows=defaultNamedNotOptArg, NumColumns=defaultNamedNotOptArg, Left=-1.0, Top=-1.0
			, Width=-1.0, Height=-1.0):
		ret = self._oleobj_.InvokeTypes(2013, LCID, 1, (9, 0), ((3, 1), (3, 1), (4, 49), (4, 49), (4, 49), (4, 49)),NumRows
			, NumColumns, Left, Top, Width, Height
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddTable', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddTextEffect(self, PresetTextEffect=defaultNamedNotOptArg, Text=defaultNamedNotOptArg, FontName=defaultNamedNotOptArg, FontSize=defaultNamedNotOptArg
			, FontBold=defaultNamedNotOptArg, FontItalic=defaultNamedNotOptArg, Left=defaultNamedNotOptArg, Top=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(18, LCID, 1, (9, 0), ((3, 1), (8, 1), (8, 1), (4, 1), (3, 1), (3, 1), (4, 1), (4, 1)),PresetTextEffect
			, Text, FontName, FontSize, FontBold, FontItalic
			, Left, Top)
		if ret is not None:
			ret = Dispatch(ret, 'AddTextEffect', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddTextbox(self, Orientation=defaultNamedNotOptArg, Left=defaultNamedNotOptArg, Top=defaultNamedNotOptArg, Width=defaultNamedNotOptArg
			, Height=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(19, LCID, 1, (9, 0), ((3, 1), (4, 1), (4, 1), (4, 1), (4, 1)),Orientation
			, Left, Top, Width, Height)
		if ret is not None:
			ret = Dispatch(ret, 'AddTextbox', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def AddTitle(self):
		ret = self._oleobj_.InvokeTypes(2005, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'AddTitle', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type FreeformBuilder
	def BuildFreeform(self, EditingType=defaultNamedNotOptArg, X1=defaultNamedNotOptArg, Y1=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(20, LCID, 1, (9, 0), ((3, 1), (4, 1), (4, 1)),EditingType
			, X1, Y1)
		if ret is not None:
			ret = Dispatch(ret, 'BuildFreeform', '{91493478-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Shape
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type ShapeRange
	def Paste(self):
		ret = self._oleobj_.InvokeTypes(2012, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Paste', '{9149347A-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type ShapeRange
	def PasteSpecial(self, DataType=0, DisplayAsIcon=0, IconFileName='', IconIndex=0
			, IconLabel='', Link=0):
		return self._ApplyTypes_(2014, 1, (9, 32), ((3, 49), (3, 49), (8, 49), (3, 49), (8, 49), (3, 49)), 'PasteSpecial', '{9149347A-5A91-11CF-8700-00AA0060263B}',DataType
			, DisplayAsIcon, IconFileName, IconIndex, IconLabel, Link
			)

	# Result is of type ShapeRange
	def Range(self, Index=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(2003, LCID, 1, (9, 0), ((12, 17),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Range', '{9149347A-5A91-11CF-8700-00AA0060263B}')
		return ret

	def SelectAll(self):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Application": (2001, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		"HasTitle": (2004, 2, (3, 0), (), "HasTitle", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'Placeholders' returns object of type 'Placeholders'
		"Placeholders": (2007, 2, (9, 0), (), "Placeholders", '{91493476-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Title' returns object of type 'Shape'
		"Title": (2006, 2, (9, 0), (), "Title", '{91493479-5A91-11CF-8700-00AA0060263B}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{91493479-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{91493479-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{91493479-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class SlideRange(DispatchBaseClass):
	CLSID = IID('{9149346B-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def ApplyTemplate(self, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2032, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def Copy(self):
		return self._oleobj_.InvokeTypes(2013, LCID, 1, (24, 0), (),)

	def Cut(self):
		return self._oleobj_.InvokeTypes(2012, LCID, 1, (24, 0), (),)

	def Delete(self):
		return self._oleobj_.InvokeTypes(2016, LCID, 1, (24, 0), (),)

	# Result is of type SlideRange
	def Duplicate(self):
		ret = self._oleobj_.InvokeTypes(2015, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', '{9149346B-5A91-11CF-8700-00AA0060263B}')
		return ret

	def Export(self, FileName=defaultNamedNotOptArg, FilterName=defaultNamedNotOptArg, ScaleWidth=0, ScaleHeight=0):
		return self._oleobj_.InvokeTypes(2025, LCID, 1, (24, 0), ((8, 1), (8, 1), (3, 49), (3, 49)),FileName
			, FilterName, ScaleWidth, ScaleHeight)

	# Result is of type Slide
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (13, 0), ((12, 1),),Index
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(global_IID_IDispatch)
			except global_error:
				return ret
			ret = Dispatch(ret, 'Item', '{91493445-5A91-11CF-8700-00AA0060263B}')
		return ret

	def MoveTo(self, toPos=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2030, LCID, 1, (24, 0), ((3, 1),),toPos
			)

	def Select(self):
		return self._oleobj_.InvokeTypes(2011, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Background' returns object of type 'ShapeRange'
		"Background": (2007, 2, (9, 0), (), "Background", '{9149347A-5A91-11CF-8700-00AA0060263B}'),
		# Method 'ColorScheme' returns object of type 'ColorScheme'
		"ColorScheme": (2006, 2, (9, 0), (), "ColorScheme", '{9149346F-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Comments' returns object of type 'Comments'
		"Comments": (2028, 2, (9, 0), (), "Comments", '{914934D4-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		# Method 'Design' returns object of type 'Design'
		"Design": (2029, 2, (9, 0), (), "Design", '{914934D7-5A91-11CF-8700-00AA0060263B}'),
		"DisplayMasterShapes": (2020, 2, (3, 0), (), "DisplayMasterShapes", None),
		"FollowMasterBackground": (2021, 2, (3, 0), (), "FollowMasterBackground", None),
		# Method 'HeadersFooters' returns object of type 'HeadersFooters'
		"HeadersFooters": (2004, 2, (9, 0), (), "HeadersFooters", '{91493474-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Hyperlinks' returns object of type 'Hyperlinks'
		"Hyperlinks": (2024, 2, (9, 0), (), "Hyperlinks", '{91493464-5A91-11CF-8700-00AA0060263B}'),
		"Layout": (2014, 2, (3, 0), (), "Layout", None),
		# Method 'Master' returns object of type '_Master'
		"Master": (2023, 2, (9, 0), (), "Master", '{9149346C-5A91-11CF-8700-00AA0060263B}'),
		"Name": (2008, 2, (8, 0), (), "Name", None),
		# Method 'NotesPage' returns object of type 'SlideRange'
		"NotesPage": (2022, 2, (9, 0), (), "NotesPage", '{9149346B-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"PrintSteps": (2010, 2, (3, 0), (), "PrintSteps", None),
		# Method 'Scripts' returns object of type 'Scripts'
		"Scripts": (2026, 2, (9, 0), (), "Scripts", '{000C0340-0000-0000-C000-000000000046}'),
		# Method 'Shapes' returns object of type 'Shapes'
		"Shapes": (2003, 2, (9, 0), (), "Shapes", '{91493475-5A91-11CF-8700-00AA0060263B}'),
		"SlideID": (2009, 2, (3, 0), (), "SlideID", None),
		"SlideIndex": (2018, 2, (3, 0), (), "SlideIndex", None),
		"SlideNumber": (2019, 2, (3, 0), (), "SlideNumber", None),
		# Method 'SlideShowTransition' returns object of type 'SlideShowTransition'
		"SlideShowTransition": (2005, 2, (9, 0), (), "SlideShowTransition", '{91493471-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Tags' returns object of type 'Tags'
		"Tags": (2017, 2, (9, 0), (), "Tags", '{914934B9-5A91-11CF-8700-00AA0060263B}'),
		# Method 'TimeLine' returns object of type 'TimeLine'
		"TimeLine": (2031, 2, (9, 0), (), "TimeLine", '{914934DC-5A91-11CF-8700-00AA0060263B}'),
	}
	_prop_map_put_ = {
		"ColorScheme": ((2006, LCID, 4, 0),()),
		"Design": ((2029, LCID, 4, 0),()),
		"DisplayMasterShapes": ((2020, LCID, 4, 0),()),
		"FollowMasterBackground": ((2021, LCID, 4, 0),()),
		"Layout": ((2014, LCID, 4, 0),()),
		"Name": ((2008, LCID, 4, 0),()),
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (13, 0), ((12, 1),),Index
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(global_IID_IDispatch)
			except global_error:
				return ret
			ret = Dispatch(ret, '__call__', '{91493445-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{91493445-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{91493445-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class SlideShowSettings(DispatchBaseClass):
	CLSID = IID('{9149345A-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type SlideShowWindow
	def Run(self):
		ret = self._oleobj_.InvokeTypes(2008, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Run', '{91493453-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		"AdvanceMode": (2007, 2, (3, 0), (), "AdvanceMode", None),
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"EndingSlide": (2006, 2, (3, 0), (), "EndingSlide", None),
		"LoopUntilStopped": (2009, 2, (3, 0), (), "LoopUntilStopped", None),
		# Method 'NamedSlideShows' returns object of type 'NamedSlideShows'
		"NamedSlideShows": (2004, 2, (9, 0), (), "NamedSlideShows", '{9149345B-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		# Method 'PointerColor' returns object of type 'ColorFormat'
		"PointerColor": (2003, 2, (9, 0), (), "PointerColor", '{91493452-5A91-11CF-8700-00AA0060263B}'),
		"RangeType": (2014, 2, (3, 0), (), "RangeType", None),
		"ShowScrollbar": (2015, 2, (3, 0), (), "ShowScrollbar", None),
		"ShowType": (2010, 2, (3, 0), (), "ShowType", None),
		"ShowWithAnimation": (2012, 2, (3, 0), (), "ShowWithAnimation", None),
		"ShowWithNarration": (2011, 2, (3, 0), (), "ShowWithNarration", None),
		"SlideShowName": (2013, 2, (8, 0), (), "SlideShowName", None),
		"StartingSlide": (2005, 2, (3, 0), (), "StartingSlide", None),
	}
	_prop_map_put_ = {
		"AdvanceMode": ((2007, LCID, 4, 0),()),
		"EndingSlide": ((2006, LCID, 4, 0),()),
		"LoopUntilStopped": ((2009, LCID, 4, 0),()),
		"RangeType": ((2014, LCID, 4, 0),()),
		"ShowScrollbar": ((2015, LCID, 4, 0),()),
		"ShowType": ((2010, LCID, 4, 0),()),
		"ShowWithAnimation": ((2012, LCID, 4, 0),()),
		"ShowWithNarration": ((2011, LCID, 4, 0),()),
		"SlideShowName": ((2013, LCID, 4, 0),()),
		"StartingSlide": ((2005, LCID, 4, 0),()),
	}

class SlideShowTransition(DispatchBaseClass):
	CLSID = IID('{91493471-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		"AdvanceOnClick": (2003, 2, (3, 0), (), "AdvanceOnClick", None),
		"AdvanceOnTime": (2004, 2, (3, 0), (), "AdvanceOnTime", None),
		"AdvanceTime": (2005, 2, (4, 0), (), "AdvanceTime", None),
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"EntryEffect": (2006, 2, (3, 0), (), "EntryEffect", None),
		"Hidden": (2007, 2, (3, 0), (), "Hidden", None),
		"LoopSoundUntilNext": (2008, 2, (3, 0), (), "LoopSoundUntilNext", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		# Method 'SoundEffect' returns object of type 'SoundEffect'
		"SoundEffect": (2009, 2, (9, 0), (), "SoundEffect", '{91493472-5A91-11CF-8700-00AA0060263B}'),
		"Speed": (2010, 2, (3, 0), (), "Speed", None),
	}
	_prop_map_put_ = {
		"AdvanceOnClick": ((2003, LCID, 4, 0),()),
		"AdvanceOnTime": ((2004, LCID, 4, 0),()),
		"AdvanceTime": ((2005, LCID, 4, 0),()),
		"EntryEffect": ((2006, LCID, 4, 0),()),
		"Hidden": ((2007, LCID, 4, 0),()),
		"LoopSoundUntilNext": ((2008, LCID, 4, 0),()),
		"Speed": ((2010, LCID, 4, 0),()),
	}

class SlideShowView(DispatchBaseClass):
	CLSID = IID('{91493459-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def DrawLine(self, BeginX=defaultNamedNotOptArg, BeginY=defaultNamedNotOptArg, EndX=defaultNamedNotOptArg, EndY=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2015, LCID, 1, (24, 0), ((4, 1), (4, 1), (4, 1), (4, 1)),BeginX
			, BeginY, EndX, EndY)

	def EndNamedShow(self):
		return self._oleobj_.InvokeTypes(2023, LCID, 1, (24, 0), (),)

	def EraseDrawing(self):
		return self._oleobj_.InvokeTypes(2016, LCID, 1, (24, 0), (),)

	def Exit(self):
		return self._oleobj_.InvokeTypes(2025, LCID, 1, (24, 0), (),)

	def First(self):
		return self._oleobj_.InvokeTypes(2017, LCID, 1, (24, 0), (),)

	def GotoNamedShow(self, SlideShowName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2022, LCID, 1, (24, 0), ((8, 1),),SlideShowName
			)

	def GotoSlide(self, Index=defaultNamedNotOptArg, ResetSlide=-1):
		return self._oleobj_.InvokeTypes(2021, LCID, 1, (24, 0), ((3, 1), (3, 49)),Index
			, ResetSlide)

	def InstallTracker(self, pTracker=defaultNamedNotOptArg, Presenter=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2026, LCID, 1, (24, 0), ((13, 1), (3, 1)),pTracker
			, Presenter)

	def Last(self):
		return self._oleobj_.InvokeTypes(2018, LCID, 1, (24, 0), (),)

	def Next(self):
		return self._oleobj_.InvokeTypes(2019, LCID, 1, (24, 0), (),)

	def Previous(self):
		return self._oleobj_.InvokeTypes(2020, LCID, 1, (24, 0), (),)

	def ResetSlideTime(self):
		return self._oleobj_.InvokeTypes(2024, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"AcceleratorsEnabled": (2007, 2, (3, 0), (), "AcceleratorsEnabled", None),
		"AdvanceMode": (2011, 2, (3, 0), (), "AdvanceMode", None),
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"CurrentShowPosition": (2027, 2, (3, 0), (), "CurrentShowPosition", None),
		"IsNamedShow": (2013, 2, (3, 0), (), "IsNamedShow", None),
		# Method 'LastSlideViewed' returns object of type 'Slide'
		"LastSlideViewed": (2010, 2, (13, 0), (), "LastSlideViewed", '{91493445-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		# Method 'PointerColor' returns object of type 'ColorFormat'
		"PointerColor": (2012, 2, (9, 0), (), "PointerColor", '{91493452-5A91-11CF-8700-00AA0060263B}'),
		"PointerType": (2005, 2, (3, 0), (), "PointerType", None),
		"PresentationElapsedTime": (2008, 2, (4, 0), (), "PresentationElapsedTime", None),
		# Method 'Slide' returns object of type 'Slide'
		"Slide": (2004, 2, (13, 0), (), "Slide", '{91493445-5A91-11CF-8700-00AA0060263B}'),
		"SlideElapsedTime": (2009, 2, (4, 0), (), "SlideElapsedTime", None),
		"SlideShowName": (2014, 2, (8, 0), (), "SlideShowName", None),
		"State": (2006, 2, (3, 0), (), "State", None),
		"Zoom": (2003, 2, (3, 0), (), "Zoom", None),
	}
	_prop_map_put_ = {
		"AcceleratorsEnabled": ((2007, LCID, 4, 0),()),
		"PointerType": ((2005, LCID, 4, 0),()),
		"SlideElapsedTime": ((2009, LCID, 4, 0),()),
		"State": ((2006, LCID, 4, 0),()),
	}

class SlideShowWindow(DispatchBaseClass):
	CLSID = IID('{91493453-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Activate(self):
		return self._oleobj_.InvokeTypes(2012, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Active": (2011, 2, (3, 0), (), "Active", None),
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"HWND": (2010, 2, (3, 0), (), "HWND", None),
		"Height": (2009, 2, (4, 0), (), "Height", None),
		"IsFullScreen": (2005, 2, (3, 0), (), "IsFullScreen", None),
		"Left": (2006, 2, (4, 0), (), "Left", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		# Method 'Presentation' returns object of type 'Presentation'
		"Presentation": (2004, 2, (13, 0), (), "Presentation", '{91493444-5A91-11CF-8700-00AA0060263B}'),
		"Top": (2007, 2, (4, 0), (), "Top", None),
		# Method 'View' returns object of type 'SlideShowView'
		"View": (2003, 2, (9, 0), (), "View", '{91493459-5A91-11CF-8700-00AA0060263B}'),
		"Width": (2008, 2, (4, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"Height": ((2009, LCID, 4, 0),()),
		"Left": ((2006, LCID, 4, 0),()),
		"Top": ((2007, LCID, 4, 0),()),
		"Width": ((2008, LCID, 4, 0),()),
	}

class SlideShowWindows(DispatchBaseClass):
	CLSID = IID('{91493456-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type SlideShowWindow
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{91493453-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{91493453-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{91493453-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{91493453-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class Slides(DispatchBaseClass):
	CLSID = IID('{91493469-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type Slide
	def Add(self, Index=defaultNamedNotOptArg, Layout=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(2004, LCID, 1, (13, 0), ((3, 1), (3, 1)),Index
			, Layout)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(global_IID_IDispatch)
			except global_error:
				return ret
			ret = Dispatch(ret, 'Add', '{91493445-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type Slide
	def FindBySlideID(self, SlideID=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(2003, LCID, 1, (13, 0), ((3, 1),),SlideID
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(global_IID_IDispatch)
			except global_error:
				return ret
			ret = Dispatch(ret, 'FindBySlideID', '{91493445-5A91-11CF-8700-00AA0060263B}')
		return ret

	def InsertFromFile(self, FileName=defaultNamedNotOptArg, Index=defaultNamedNotOptArg, SlideStart=1, SlideEnd=-1):
		return self._oleobj_.InvokeTypes(2005, LCID, 1, (3, 0), ((8, 1), (3, 1), (3, 49), (3, 49)),FileName
			, Index, SlideStart, SlideEnd)

	# Result is of type Slide
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (13, 0), ((12, 1),),Index
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(global_IID_IDispatch)
			except global_error:
				return ret
			ret = Dispatch(ret, 'Item', '{91493445-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type SlideRange
	def Paste(self, Index=-1):
		ret = self._oleobj_.InvokeTypes(2007, LCID, 1, (9, 0), ((3, 49),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Paste', '{9149346B-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type SlideRange
	def Range(self, Index=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(2006, LCID, 1, (9, 0), ((12, 17),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Range', '{9149346B-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (13, 0), ((12, 1),),Index
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(global_IID_IDispatch)
			except global_error:
				return ret
			ret = Dispatch(ret, '__call__', '{91493445-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{91493445-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{91493445-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class SoundEffect(DispatchBaseClass):
	CLSID = IID('{91493472-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def ImportFromFile(self, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2005, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def Play(self):
		return self._oleobj_.InvokeTypes(2006, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Name": (2003, 2, (8, 0), (), "Name", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Type": (2004, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Name": ((2003, LCID, 4, 0),()),
		"Type": ((2004, LCID, 4, 0),()),
	}

class SoundFormat(DispatchBaseClass):
	CLSID = IID('{91493473-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Export(self, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2002, LCID, 1, (3, 0), ((8, 1),),FileName
			)

	def Import(self, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2001, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def Play(self):
		return self._oleobj_.InvokeTypes(2000, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"SourceFullName": (2004, 2, (8, 0), (), "SourceFullName", None),
		"Type": (2003, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
	}

class TabStop(DispatchBaseClass):
	CLSID = IID('{91493494-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Clear(self):
		return self._oleobj_.InvokeTypes(2005, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Position": (2004, 2, (4, 0), (), "Position", None),
		"Type": (2003, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Position": ((2004, LCID, 4, 0),()),
		"Type": ((2003, LCID, 4, 0),()),
	}

class TabStops(DispatchBaseClass):
	CLSID = IID('{91493493-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type TabStop
	def Add(self, Type=defaultNamedNotOptArg, Position=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(2004, LCID, 1, (9, 0), ((3, 1), (4, 1)),Type
			, Position)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{91493494-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type TabStop
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{91493494-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"DefaultSpacing": (2003, 2, (4, 0), (), "DefaultSpacing", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"DefaultSpacing": ((2003, LCID, 4, 0),()),
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{91493494-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{91493494-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{91493494-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class Table(DispatchBaseClass):
	CLSID = IID('{914934C3-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type Cell
	def Cell(self, Row=defaultNamedNotOptArg, Column=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(2005, LCID, 1, (9, 0), ((3, 1), (3, 1)),Row
			, Column)
		if ret is not None:
			ret = Dispatch(ret, 'Cell', '{914934C9-5A91-11CF-8700-00AA0060263B}')
		return ret

	def MergeBorders(self):
		return self._oleobj_.InvokeTypes(2007, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Columns' returns object of type 'Columns'
		"Columns": (2003, 2, (9, 0), (), "Columns", '{914934C4-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		# Method 'Rows' returns object of type 'Rows'
		"Rows": (2004, 2, (9, 0), (), "Rows", '{914934C6-5A91-11CF-8700-00AA0060263B}'),
		"TableDirection": (2006, 2, (3, 0), (), "TableDirection", None),
	}
	_prop_map_put_ = {
		"TableDirection": ((2006, LCID, 4, 0),()),
	}

class Tags(DispatchBaseClass):
	CLSID = IID('{914934B9-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def Add(self, Name=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2003, LCID, 1, (24, 0), ((8, 1), (8, 1)),Name
			, Value)

	def AddBinary(self, Name=defaultNamedNotOptArg, FilePath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2005, LCID, 1, (24, 0), ((8, 1), (8, 1)),Name
			, FilePath)

	def BinaryValue(self, Name=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2006, LCID, 1, (3, 0), ((8, 1),),Name
			)

	def Delete(self, Name=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2004, LCID, 1, (24, 0), ((8, 1),),Name
			)

	def Item(self, Name=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(0, LCID, 1, (8, 0), ((8, 1),),Name
			)

	def Name(self, Index=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(2007, LCID, 1, (8, 0), ((3, 1),),Index
			)

	def Value(self, Index=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(2008, LCID, 1, (8, 0), ((3, 1),),Index
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Name=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(0, LCID, 1, (8, 0), ((8, 1),),Name
			)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, None)
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),None)
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class TextEffectFormat(DispatchBaseClass):
	CLSID = IID('{91493482-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def ToggleVerticalText(self):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Alignment": (100, 2, (3, 0), (), "Alignment", None),
		"Application": (2001, 2, (9, 0), (), "Application", None),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		"FontBold": (101, 2, (3, 0), (), "FontBold", None),
		"FontItalic": (102, 2, (3, 0), (), "FontItalic", None),
		"FontName": (103, 2, (8, 0), (), "FontName", None),
		"FontSize": (104, 2, (4, 0), (), "FontSize", None),
		"KernedPairs": (105, 2, (3, 0), (), "KernedPairs", None),
		"NormalizedHeight": (106, 2, (3, 0), (), "NormalizedHeight", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		"PresetShape": (107, 2, (3, 0), (), "PresetShape", None),
		"PresetTextEffect": (108, 2, (3, 0), (), "PresetTextEffect", None),
		"RotatedChars": (109, 2, (3, 0), (), "RotatedChars", None),
		"Text": (110, 2, (8, 0), (), "Text", None),
		"Tracking": (111, 2, (4, 0), (), "Tracking", None),
	}
	_prop_map_put_ = {
		"Alignment": ((100, LCID, 4, 0),()),
		"FontBold": ((101, LCID, 4, 0),()),
		"FontItalic": ((102, LCID, 4, 0),()),
		"FontName": ((103, LCID, 4, 0),()),
		"FontSize": ((104, LCID, 4, 0),()),
		"KernedPairs": ((105, LCID, 4, 0),()),
		"NormalizedHeight": ((106, LCID, 4, 0),()),
		"PresetShape": ((107, LCID, 4, 0),()),
		"PresetTextEffect": ((108, LCID, 4, 0),()),
		"RotatedChars": ((109, LCID, 4, 0),()),
		"Text": ((110, LCID, 4, 0),()),
		"Tracking": ((111, LCID, 4, 0),()),
	}

class TextFrame(DispatchBaseClass):
	CLSID = IID('{91493484-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def DeleteText(self):
		return self._oleobj_.InvokeTypes(2010, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Application": (2001, 2, (9, 0), (), "Application", None),
		"AutoSize": (2008, 2, (3, 0), (), "AutoSize", None),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		"HasText": (2003, 2, (3, 0), (), "HasText", None),
		"HorizontalAnchor": (2006, 2, (3, 0), (), "HorizontalAnchor", None),
		"MarginBottom": (100, 2, (4, 0), (), "MarginBottom", None),
		"MarginLeft": (101, 2, (4, 0), (), "MarginLeft", None),
		"MarginRight": (102, 2, (4, 0), (), "MarginRight", None),
		"MarginTop": (103, 2, (4, 0), (), "MarginTop", None),
		"Orientation": (104, 2, (3, 0), (), "Orientation", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'Ruler' returns object of type 'Ruler'
		"Ruler": (2005, 2, (9, 0), (), "Ruler", '{91493490-5A91-11CF-8700-00AA0060263B}'),
		# Method 'TextRange' returns object of type 'TextRange'
		"TextRange": (2004, 2, (9, 0), (), "TextRange", '{9149348F-5A91-11CF-8700-00AA0060263B}'),
		"VerticalAnchor": (2007, 2, (3, 0), (), "VerticalAnchor", None),
		"WordWrap": (2009, 2, (3, 0), (), "WordWrap", None),
	}
	_prop_map_put_ = {
		"AutoSize": ((2008, LCID, 4, 0),()),
		"HorizontalAnchor": ((2006, LCID, 4, 0),()),
		"MarginBottom": ((100, LCID, 4, 0),()),
		"MarginLeft": ((101, LCID, 4, 0),()),
		"MarginRight": ((102, LCID, 4, 0),()),
		"MarginTop": ((103, LCID, 4, 0),()),
		"Orientation": ((104, LCID, 4, 0),()),
		"VerticalAnchor": ((2007, LCID, 4, 0),()),
		"WordWrap": ((2009, LCID, 4, 0),()),
	}

class TextRange(DispatchBaseClass):
	CLSID = IID('{9149348F-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def AddPeriods(self):
		return self._oleobj_.InvokeTypes(2031, LCID, 1, (24, 0), (),)

	def ChangeCase(self, Type=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2030, LCID, 1, (24, 0), ((3, 1),),Type
			)

	# Result is of type TextRange
	def Characters(self, Start=-1, Length=-1):
		ret = self._oleobj_.InvokeTypes(2013, LCID, 1, (9, 0), ((3, 49), (3, 49)),Start
			, Length)
		if ret is not None:
			ret = Dispatch(ret, 'Characters', '{9149348F-5A91-11CF-8700-00AA0060263B}')
		return ret

	def Copy(self):
		return self._oleobj_.InvokeTypes(2027, LCID, 1, (24, 0), (),)

	def Cut(self):
		return self._oleobj_.InvokeTypes(2026, LCID, 1, (24, 0), (),)

	def Delete(self):
		return self._oleobj_.InvokeTypes(2028, LCID, 1, (24, 0), (),)

	# Result is of type TextRange
	def Find(self, FindWhat=defaultNamedNotOptArg, After=0, MatchCase=0, WholeWords=0):
		ret = self._oleobj_.InvokeTypes(2033, LCID, 1, (9, 0), ((8, 1), (3, 49), (3, 49), (3, 49)),FindWhat
			, After, MatchCase, WholeWords)
		if ret is not None:
			ret = Dispatch(ret, 'Find', '{9149348F-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type TextRange
	def InsertAfter(self, NewText=''):
		return self._ApplyTypes_(2017, 1, (9, 32), ((8, 49),), 'InsertAfter', '{9149348F-5A91-11CF-8700-00AA0060263B}',NewText
			)

	# Result is of type TextRange
	def InsertBefore(self, NewText=''):
		return self._ApplyTypes_(2018, 1, (9, 32), ((8, 49),), 'InsertBefore', '{9149348F-5A91-11CF-8700-00AA0060263B}',NewText
			)

	# Result is of type TextRange
	def InsertDateTime(self, DateTimeFormat=defaultNamedNotOptArg, InsertAsField=0):
		ret = self._oleobj_.InvokeTypes(2019, LCID, 1, (9, 0), ((3, 1), (3, 49)),DateTimeFormat
			, InsertAsField)
		if ret is not None:
			ret = Dispatch(ret, 'InsertDateTime', '{9149348F-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type TextRange
	def InsertSlideNumber(self):
		ret = self._oleobj_.InvokeTypes(2020, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'InsertSlideNumber', '{9149348F-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type TextRange
	def InsertSymbol(self, FontName=defaultNamedNotOptArg, CharNumber=defaultNamedNotOptArg, Unicode=0):
		ret = self._oleobj_.InvokeTypes(2021, LCID, 1, (9, 0), ((8, 1), (3, 1), (3, 49)),FontName
			, CharNumber, Unicode)
		if ret is not None:
			ret = Dispatch(ret, 'InsertSymbol', '{9149348F-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type TextRange
	def Lines(self, Start=-1, Length=-1):
		ret = self._oleobj_.InvokeTypes(2014, LCID, 1, (9, 0), ((3, 49), (3, 49)),Start
			, Length)
		if ret is not None:
			ret = Dispatch(ret, 'Lines', '{9149348F-5A91-11CF-8700-00AA0060263B}')
		return ret

	def LtrRun(self):
		return self._oleobj_.InvokeTypes(2038, LCID, 1, (24, 0), (),)

	# Result is of type TextRange
	def Paragraphs(self, Start=-1, Length=-1):
		ret = self._oleobj_.InvokeTypes(2010, LCID, 1, (9, 0), ((3, 49), (3, 49)),Start
			, Length)
		if ret is not None:
			ret = Dispatch(ret, 'Paragraphs', '{9149348F-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type TextRange
	def Paste(self):
		ret = self._oleobj_.InvokeTypes(2029, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Paste', '{9149348F-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type TextRange
	def PasteSpecial(self, DataType=0, DisplayAsIcon=0, IconFileName='', IconIndex=0
			, IconLabel='', Link=0):
		return self._ApplyTypes_(2039, 1, (9, 32), ((3, 49), (3, 49), (8, 49), (3, 49), (8, 49), (3, 49)), 'PasteSpecial', '{9149348F-5A91-11CF-8700-00AA0060263B}',DataType
			, DisplayAsIcon, IconFileName, IconIndex, IconLabel, Link
			)

	def RemovePeriods(self):
		return self._oleobj_.InvokeTypes(2032, LCID, 1, (24, 0), (),)

	# Result is of type TextRange
	def Replace(self, FindWhat=defaultNamedNotOptArg, ReplaceWhat=defaultNamedNotOptArg, After=0, MatchCase=0
			, WholeWords=0):
		ret = self._oleobj_.InvokeTypes(2034, LCID, 1, (9, 0), ((8, 1), (8, 1), (3, 49), (3, 49), (3, 49)),FindWhat
			, ReplaceWhat, After, MatchCase, WholeWords)
		if ret is not None:
			ret = Dispatch(ret, 'Replace', '{9149348F-5A91-11CF-8700-00AA0060263B}')
		return ret

	def RotatedBounds(self, X1=global_Missing, Y1=global_Missing, X2=global_Missing, Y2=global_Missing
			, X3=global_Missing, Y3=global_Missing, x4=global_Missing, y4=global_Missing):
		return self._ApplyTypes_(2035, 1, (24, 0), ((16388, 2), (16388, 2), (16388, 2), (16388, 2), (16388, 2), (16388, 2), (16388, 2), (16388, 2)), 'RotatedBounds', None,X1
			, Y1, X2, Y2, X3, Y3
			, x4, y4)

	def RtlRun(self):
		return self._oleobj_.InvokeTypes(2037, LCID, 1, (24, 0), (),)

	# Result is of type TextRange
	def Runs(self, Start=-1, Length=-1):
		ret = self._oleobj_.InvokeTypes(2015, LCID, 1, (9, 0), ((3, 49), (3, 49)),Start
			, Length)
		if ret is not None:
			ret = Dispatch(ret, 'Runs', '{9149348F-5A91-11CF-8700-00AA0060263B}')
		return ret

	def Select(self):
		return self._oleobj_.InvokeTypes(2025, LCID, 1, (24, 0), (),)

	# Result is of type TextRange
	def Sentences(self, Start=-1, Length=-1):
		ret = self._oleobj_.InvokeTypes(2011, LCID, 1, (9, 0), ((3, 49), (3, 49)),Start
			, Length)
		if ret is not None:
			ret = Dispatch(ret, 'Sentences', '{9149348F-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type TextRange
	def TrimText(self):
		ret = self._oleobj_.InvokeTypes(2016, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'TrimText', '{9149348F-5A91-11CF-8700-00AA0060263B}')
		return ret

	# Result is of type TextRange
	def Words(self, Start=-1, Length=-1):
		ret = self._oleobj_.InvokeTypes(2012, LCID, 1, (9, 0), ((3, 49), (3, 49)),Start
			, Length)
		if ret is not None:
			ret = Dispatch(ret, 'Words', '{9149348F-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'ActionSettings' returns object of type 'ActionSettings'
		"ActionSettings": (2003, 2, (9, 0), (), "ActionSettings", '{9149348C-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"BoundHeight": (2009, 2, (4, 0), (), "BoundHeight", None),
		"BoundLeft": (2006, 2, (4, 0), (), "BoundLeft", None),
		"BoundTop": (2007, 2, (4, 0), (), "BoundTop", None),
		"BoundWidth": (2008, 2, (4, 0), (), "BoundWidth", None),
		"Count": (11, 2, (3, 0), (), "Count", None),
		# Method 'Font' returns object of type 'Font'
		"Font": (2022, 2, (9, 0), (), "Font", '{91493495-5A91-11CF-8700-00AA0060263B}'),
		"IndentLevel": (2024, 2, (3, 0), (), "IndentLevel", None),
		"LanguageID": (2036, 2, (3, 0), (), "LanguageID", None),
		"Length": (2005, 2, (3, 0), (), "Length", None),
		# Method 'ParagraphFormat' returns object of type 'ParagraphFormat'
		"ParagraphFormat": (2023, 2, (9, 0), (), "ParagraphFormat", '{91493496-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Start": (2004, 2, (3, 0), (), "Start", None),
		"Text": (0, 2, (8, 0), (), "Text", None),
	}
	_prop_map_put_ = {
		"IndentLevel": ((2024, LCID, 4, 0),()),
		"LanguageID": ((2036, LCID, 4, 0),()),
		"Text": ((0, LCID, 4, 0),()),
	}
	# Default property for this class is 'Text'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Text", None))
	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, None)
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),None)
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class TextStyle(DispatchBaseClass):
	CLSID = IID('{91493499-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Levels' returns object of type 'TextStyleLevels'
		"Levels": (2005, 2, (9, 0), (), "Levels", '{9149349A-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		# Method 'Ruler' returns object of type 'Ruler'
		"Ruler": (2003, 2, (9, 0), (), "Ruler", '{91493490-5A91-11CF-8700-00AA0060263B}'),
		# Method 'TextFrame' returns object of type 'TextFrame'
		"TextFrame": (2004, 2, (9, 0), (), "TextFrame", '{91493484-5A91-11CF-8700-00AA0060263B}'),
	}
	_prop_map_put_ = {
	}

class TextStyleLevel(DispatchBaseClass):
	CLSID = IID('{9149349B-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Font' returns object of type 'Font'
		"Font": (2004, 2, (9, 0), (), "Font", '{91493495-5A91-11CF-8700-00AA0060263B}'),
		# Method 'ParagraphFormat' returns object of type 'ParagraphFormat'
		"ParagraphFormat": (2003, 2, (9, 0), (), "ParagraphFormat", '{91493496-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}

class TextStyleLevels(DispatchBaseClass):
	CLSID = IID('{9149349A-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type TextStyleLevel
	def Item(self, Level=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Level
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{9149349B-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Level=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Level
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{9149349B-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{9149349B-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{9149349B-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class TextStyles(DispatchBaseClass):
	CLSID = IID('{91493498-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	# Result is of type TextStyle
	def Item(self, Type=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Type
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{91493499-5A91-11CF-8700-00AA0060263B}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"Count": (11, 2, (3, 0), (), "Count", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Type=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Type
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{91493499-5A91-11CF-8700-00AA0060263B}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{91493499-5A91-11CF-8700-00AA0060263B}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{91493499-5A91-11CF-8700-00AA0060263B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(11, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class ThreeDFormat(DispatchBaseClass):
	CLSID = IID('{91493483-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def IncrementRotationX(self, Increment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((4, 1),),Increment
			)

	def IncrementRotationY(self, Increment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((4, 1),),Increment
			)

	def ResetRotation(self):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), (),)

	def SetExtrusionDirection(self, PresetExtrusionDirection=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((3, 1),),PresetExtrusionDirection
			)

	def SetThreeDFormat(self, PresetThreeDFormat=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((3, 1),),PresetThreeDFormat
			)

	_prop_map_get_ = {
		"Application": (2001, 2, (9, 0), (), "Application", None),
		"Creator": (2002, 2, (3, 0), (), "Creator", None),
		"Depth": (100, 2, (4, 0), (), "Depth", None),
		# Method 'ExtrusionColor' returns object of type 'ColorFormat'
		"ExtrusionColor": (101, 2, (9, 0), (), "ExtrusionColor", '{91493452-5A91-11CF-8700-00AA0060263B}'),
		"ExtrusionColorType": (102, 2, (3, 0), (), "ExtrusionColorType", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		"Perspective": (103, 2, (3, 0), (), "Perspective", None),
		"PresetExtrusionDirection": (104, 2, (3, 0), (), "PresetExtrusionDirection", None),
		"PresetLightingDirection": (105, 2, (3, 0), (), "PresetLightingDirection", None),
		"PresetLightingSoftness": (106, 2, (3, 0), (), "PresetLightingSoftness", None),
		"PresetMaterial": (107, 2, (3, 0), (), "PresetMaterial", None),
		"PresetThreeDFormat": (108, 2, (3, 0), (), "PresetThreeDFormat", None),
		"RotationX": (109, 2, (4, 0), (), "RotationX", None),
		"RotationY": (110, 2, (4, 0), (), "RotationY", None),
		"Visible": (111, 2, (3, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Depth": ((100, LCID, 4, 0),()),
		"ExtrusionColorType": ((102, LCID, 4, 0),()),
		"Perspective": ((103, LCID, 4, 0),()),
		"PresetLightingDirection": ((105, LCID, 4, 0),()),
		"PresetLightingSoftness": ((106, LCID, 4, 0),()),
		"PresetMaterial": ((107, LCID, 4, 0),()),
		"RotationX": ((109, LCID, 4, 0),()),
		"RotationY": ((110, LCID, 4, 0),()),
		"Visible": ((111, LCID, 4, 0),()),
	}

class TimeLine(DispatchBaseClass):
	CLSID = IID('{914934DC-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		# Method 'InteractiveSequences' returns object of type 'Sequences'
		"InteractiveSequences": (2004, 2, (9, 0), (), "InteractiveSequences", '{914934DD-5A91-11CF-8700-00AA0060263B}'),
		# Method 'MainSequence' returns object of type 'Sequence'
		"MainSequence": (2003, 2, (9, 0), (), "MainSequence", '{914934DE-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}

class Timing(DispatchBaseClass):
	CLSID = IID('{914934E0-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Accelerate": (2010, 2, (4, 0), (), "Accelerate", None),
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"AutoReverse": (2012, 2, (3, 0), (), "AutoReverse", None),
		"Decelerate": (2011, 2, (4, 0), (), "Decelerate", None),
		"Duration": (2003, 2, (4, 0), (), "Duration", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"RepeatCount": (2007, 2, (3, 0), (), "RepeatCount", None),
		"RepeatDuration": (2008, 2, (4, 0), (), "RepeatDuration", None),
		"Restart": (2016, 2, (3, 0), (), "Restart", None),
		"RewindAtEnd": (2015, 2, (3, 0), (), "RewindAtEnd", None),
		"SmoothEnd": (2014, 2, (3, 0), (), "SmoothEnd", None),
		"SmoothStart": (2013, 2, (3, 0), (), "SmoothStart", None),
		"Speed": (2009, 2, (4, 0), (), "Speed", None),
		"TriggerDelayTime": (2005, 2, (4, 0), (), "TriggerDelayTime", None),
		# Method 'TriggerShape' returns object of type 'Shape'
		"TriggerShape": (2006, 2, (9, 0), (), "TriggerShape", '{91493479-5A91-11CF-8700-00AA0060263B}'),
		"TriggerType": (2004, 2, (3, 0), (), "TriggerType", None),
	}
	_prop_map_put_ = {
		"Accelerate": ((2010, LCID, 4, 0),()),
		"AutoReverse": ((2012, LCID, 4, 0),()),
		"Decelerate": ((2011, LCID, 4, 0),()),
		"Duration": ((2003, LCID, 4, 0),()),
		"RepeatCount": ((2007, LCID, 4, 0),()),
		"RepeatDuration": ((2008, LCID, 4, 0),()),
		"Restart": ((2016, LCID, 4, 0),()),
		"RewindAtEnd": ((2015, LCID, 4, 0),()),
		"SmoothEnd": ((2014, LCID, 4, 0),()),
		"SmoothStart": ((2013, LCID, 4, 0),()),
		"Speed": ((2009, LCID, 4, 0),()),
		"TriggerDelayTime": ((2005, LCID, 4, 0),()),
		"TriggerShape": ((2006, LCID, 4, 0),()),
		"TriggerType": ((2004, LCID, 4, 0),()),
	}

class View(DispatchBaseClass):
	CLSID = IID('{91493458-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def GotoSlide(self, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2007, LCID, 1, (24, 0), ((3, 1),),Index
			)

	def Paste(self):
		return self._oleobj_.InvokeTypes(2005, LCID, 1, (24, 0), (),)

	def PasteSpecial(self, DataType=0, DisplayAsIcon=0, IconFileName='', IconIndex=0
			, IconLabel='', Link=0):
		return self._ApplyTypes_(2010, 1, (24, 32), ((3, 49), (3, 49), (8, 49), (3, 49), (8, 49), (3, 49)), 'PasteSpecial', None,DataType
			, DisplayAsIcon, IconFileName, IconIndex, IconLabel, Link
			)

	def PrintOut(self, From=-1, To=-1, PrintToFile='', Copies=0
			, Collate=-99):
		return self._ApplyTypes_(2012, 1, (24, 32), ((3, 49), (3, 49), (8, 49), (3, 49), (3, 49)), 'PrintOut', None,From
			, To, PrintToFile, Copies, Collate)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"DisplaySlideMiniature": (2008, 2, (3, 0), (), "DisplaySlideMiniature", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		# Method 'PrintOptions' returns object of type 'PrintOptions'
		"PrintOptions": (2011, 2, (9, 0), (), "PrintOptions", '{9149345D-5A91-11CF-8700-00AA0060263B}'),
		"Slide": (2006, 2, (9, 0), (), "Slide", None),
		"Type": (2003, 2, (3, 0), (), "Type", None),
		"Zoom": (2004, 2, (3, 0), (), "Zoom", None),
		"ZoomToFit": (2009, 2, (3, 0), (), "ZoomToFit", None),
	}
	_prop_map_put_ = {
		"DisplaySlideMiniature": ((2008, LCID, 4, 0),()),
		"Slide": ((2006, LCID, 4, 0),()),
		"Zoom": ((2004, LCID, 4, 0),()),
		"ZoomToFit": ((2009, LCID, 4, 0),()),
	}

class WebOptions(DispatchBaseClass):
	CLSID = IID('{914934CE-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = None

	def UseDefaultFolderSuffix(self):
		return self._oleobj_.InvokeTypes(2012, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"AllowPNG": (2008, 2, (3, 0), (), "AllowPNG", None),
		"Encoding": (2010, 2, (3, 0), (), "Encoding", None),
		"FolderSuffix": (2011, 2, (8, 0), (), "FolderSuffix", None),
		"FrameColors": (2002, 2, (3, 0), (), "FrameColors", None),
		"HTMLVersion": (2014, 2, (3, 0), (), "HTMLVersion", None),
		"IncludeNavigation": (2001, 2, (3, 0), (), "IncludeNavigation", None),
		"OrganizeInFolder": (2005, 2, (3, 0), (), "OrganizeInFolder", None),
		"RelyOnVML": (2007, 2, (3, 0), (), "RelyOnVML", None),
		"ResizeGraphics": (2003, 2, (3, 0), (), "ResizeGraphics", None),
		"ScreenSize": (2009, 2, (3, 0), (), "ScreenSize", None),
		"ShowSlideAnimation": (2004, 2, (3, 0), (), "ShowSlideAnimation", None),
		"TargetBrowser": (2013, 2, (3, 0), (), "TargetBrowser", None),
		"UseLongFileNames": (2006, 2, (3, 0), (), "UseLongFileNames", None),
	}
	_prop_map_put_ = {
		"AllowPNG": ((2008, LCID, 4, 0),()),
		"Encoding": ((2010, LCID, 4, 0),()),
		"FrameColors": ((2002, LCID, 4, 0),()),
		"HTMLVersion": ((2014, LCID, 4, 0),()),
		"IncludeNavigation": ((2001, LCID, 4, 0),()),
		"OrganizeInFolder": ((2005, LCID, 4, 0),()),
		"RelyOnVML": ((2007, LCID, 4, 0),()),
		"ResizeGraphics": ((2003, LCID, 4, 0),()),
		"ScreenSize": ((2009, LCID, 4, 0),()),
		"ShowSlideAnimation": ((2004, LCID, 4, 0),()),
		"TargetBrowser": ((2013, LCID, 4, 0),()),
		"UseLongFileNames": ((2006, LCID, 4, 0),()),
	}

class _Application(DispatchBaseClass):
	CLSID = IID('{91493442-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = IID('{91493441-5A91-11CF-8700-00AA0060263B}')

	def Activate(self):
		return self._oleobj_.InvokeTypes(2033, LCID, 1, (24, 0), (),)

	# Result is of type FileDialog
	# The method FileDialog is actually a property, but must be used as a method to correctly pass the arguments
	def FileDialog(self, Type=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(2045, LCID, 2, (9, 0), ((3, 1),),Type
			)
		if ret is not None:
			ret = Dispatch(ret, 'FileDialog', '{000C0362-0000-0000-C000-000000000046}')
		return ret

	def GetOptionFlag(self, Option=defaultNamedNotOptArg, Persist=False):
		return self._oleobj_.InvokeTypes(2043, LCID, 1, (11, 0), ((3, 1), (11, 49)),Option
			, Persist)

	def Help(self, HelpFile='vbapp10.chm', ContextID=0):
		return self._ApplyTypes_(2020, 1, (24, 32), ((8, 49), (3, 49)), 'Help', None,HelpFile
			, ContextID)

	def PPFileDialog(self, Type=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(2023, LCID, 1, (13, 0), ((3, 1),),Type
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(global_IID_IDispatch)
			except global_error:
				return ret
			ret = Dispatch(ret, 'PPFileDialog', None)
		return ret

	def Quit(self):
		return self._oleobj_.InvokeTypes(2021, LCID, 1, (24, 0), (),)

	def Run(self, *args):
		return self._get_good_object_(self._oleobj_.Invoke(*((2022,0,1,1)+args)),'Run')

	def SetOptionFlag(self, Option=defaultNamedNotOptArg, State=defaultNamedNotOptArg, Persist=False):
		return self._oleobj_.InvokeTypes(2044, LCID, 1, (24, 0), ((3, 1), (11, 1), (11, 49)),Option
			, State, Persist)

	def SetPerfMarker(self, Marker=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2051, LCID, 1, (24, 0), ((3, 1),),Marker
			)

	_prop_map_get_ = {
		"Active": (2032, 2, (3, 0), (), "Active", None),
		# Method 'ActivePresentation' returns object of type 'Presentation'
		"ActivePresentation": (2005, 2, (13, 0), (), "ActivePresentation", '{91493444-5A91-11CF-8700-00AA0060263B}'),
		"ActivePrinter": (2016, 2, (8, 0), (), "ActivePrinter", None),
		# Method 'ActiveWindow' returns object of type 'DocumentWindow'
		"ActiveWindow": (2004, 2, (9, 0), (), "ActiveWindow", '{91493457-5A91-11CF-8700-00AA0060263B}'),
		# Method 'AddIns' returns object of type 'AddIns'
		"AddIns": (2018, 2, (9, 0), (), "AddIns", '{91493460-5A91-11CF-8700-00AA0060263B}'),
		# Method 'AnswerWizard' returns object of type 'AnswerWizard'
		"AnswerWizard": (2034, 2, (9, 0), (), "AnswerWizard", '{000C0360-0000-0000-C000-000000000046}'),
		# Method 'Assistant' returns object of type 'Assistant'
		"Assistant": (2010, 2, (9, 0), (), "Assistant", '{000C0322-0000-0000-C000-000000000046}'),
		# Method 'AutoCorrect' returns object of type 'AutoCorrect'
		"AutoCorrect": (2052, 2, (9, 0), (), "AutoCorrect", '{914934ED-5A91-11CF-8700-00AA0060263B}'),
		"AutomationSecurity": (2047, 2, (3, 0), (), "AutomationSecurity", None),
		"Build": (2013, 2, (8, 0), (), "Build", None),
		# Method 'COMAddIns' returns object of type 'COMAddIns'
		"COMAddIns": (2035, 2, (9, 0), (), "COMAddIns", '{000C0339-0000-0000-C000-000000000046}'),
		"Caption": (2009, 2, (8, 0), (), "Caption", None),
		# Method 'CommandBars' returns object of type 'CommandBars'
		"CommandBars": (2007, 2, (13, 0), (), "CommandBars", '{55F88893-7708-11D1-ACEB-006008961DA5}'),
		"Creator": (2017, 2, (3, 0), (), "Creator", None),
		# Method 'DefaultWebOptions' returns object of type 'DefaultWebOptions'
		"DefaultWebOptions": (2037, 2, (9, 0), (), "DefaultWebOptions", '{914934CD-5A91-11CF-8700-00AA0060263B}'),
		"Dialogs": (2003, 2, (13, 0), (), "Dialogs", None),
		"DisplayAlerts": (2049, 2, (3, 0), (), "DisplayAlerts", None),
		"DisplayGridLines": (2046, 2, (3, 0), (), "DisplayGridLines", None),
		"FeatureInstall": (2042, 2, (3, 0), (), "FeatureInstall", None),
		# Method 'FileFind' returns object of type 'IFind'
		"FileFind": (2012, 2, (9, 0), (), "FileFind", '{000C0337-0000-0000-C000-000000000046}'),
		# Method 'FileSearch' returns object of type 'FileSearch'
		"FileSearch": (2011, 2, (9, 0), (), "FileSearch", '{000C0332-0000-0000-C000-000000000046}'),
		"HWND": (2031, 2, (3, 0), (), "HWND", None),
		"Height": (2028, 2, (4, 0), (), "Height", None),
		# Method 'LanguageSettings' returns object of type 'LanguageSettings'
		"LanguageSettings": (2038, 2, (9, 0), (), "LanguageSettings", '{000C0353-0000-0000-C000-000000000046}'),
		"Left": (2025, 2, (4, 0), (), "Left", None),
		"Marker": (2041, 2, (13, 0), (), "Marker", None),
		# Method 'MsoDebugOptions' returns object of type 'MsoDebugOptions'
		"MsoDebugOptions": (2039, 2, (9, 0), (), "MsoDebugOptions", '{000C035A-0000-0000-C000-000000000046}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		# Method 'NewPresentation' returns object of type 'NewFile'
		"NewPresentation": (2048, 2, (9, 0), (), "NewPresentation", '{000C0936-0000-0000-C000-000000000046}'),
		"OperatingSystem": (2015, 2, (8, 0), (), "OperatingSystem", None),
		# Method 'Options' returns object of type 'Options'
		"Options": (2053, 2, (9, 0), (), "Options", '{914934EE-5A91-11CF-8700-00AA0060263B}'),
		"Path": (2008, 2, (8, 0), (), "Path", None),
		# Method 'Presentations' returns object of type 'Presentations'
		"Presentations": (2001, 2, (9, 0), (), "Presentations", '{91493462-5A91-11CF-8700-00AA0060263B}'),
		"ProductCode": (2036, 2, (8, 0), (), "ProductCode", None),
		"ShowStartupDialog": (2050, 2, (3, 0), (), "ShowStartupDialog", None),
		"ShowWindowsInTaskbar": (2040, 2, (3, 0), (), "ShowWindowsInTaskbar", None),
		# Method 'SlideShowWindows' returns object of type 'SlideShowWindows'
		"SlideShowWindows": (2006, 2, (9, 0), (), "SlideShowWindows", '{91493456-5A91-11CF-8700-00AA0060263B}'),
		"Top": (2026, 2, (4, 0), (), "Top", None),
		# Method 'VBE' returns object of type 'VBE'
		"VBE": (2019, 2, (9, 0), (), "VBE", '{0002E166-0000-0000-C000-000000000046}'),
		"Version": (2014, 2, (8, 0), (), "Version", None),
		"Visible": (2030, 2, (3, 0), (), "Visible", None),
		"Width": (2027, 2, (4, 0), (), "Width", None),
		"WindowState": (2029, 2, (3, 0), (), "WindowState", None),
		# Method 'Windows' returns object of type 'DocumentWindows'
		"Windows": (2002, 2, (9, 0), (), "Windows", '{91493455-5A91-11CF-8700-00AA0060263B}'),
	}
	_prop_map_put_ = {
		"AutomationSecurity": ((2047, LCID, 4, 0),()),
		"Caption": ((2009, LCID, 4, 0),()),
		"DisplayAlerts": ((2049, LCID, 4, 0),()),
		"DisplayGridLines": ((2046, LCID, 4, 0),()),
		"FeatureInstall": ((2042, LCID, 4, 0),()),
		"Height": ((2028, LCID, 4, 0),()),
		"Left": ((2025, LCID, 4, 0),()),
		"ShowStartupDialog": ((2050, LCID, 4, 0),()),
		"ShowWindowsInTaskbar": ((2040, LCID, 4, 0),()),
		"Top": ((2026, LCID, 4, 0),()),
		"Visible": ((2030, LCID, 4, 0),()),
		"Width": ((2027, LCID, 4, 0),()),
		"WindowState": ((2029, LCID, 4, 0),()),
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return str(self.__call__(*args))
		except global_com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _Global(DispatchBaseClass):
	CLSID = IID('{91493451-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = IID('{91493443-5A91-11CF-8700-00AA0060263B}')

	_prop_map_get_ = {
		# Method 'ActivePresentation' returns object of type 'Presentation'
		"ActivePresentation": (2001, 2, (13, 0), (), "ActivePresentation", '{91493444-5A91-11CF-8700-00AA0060263B}'),
		# Method 'ActiveWindow' returns object of type 'DocumentWindow'
		"ActiveWindow": (2002, 2, (9, 0), (), "ActiveWindow", '{91493457-5A91-11CF-8700-00AA0060263B}'),
		# Method 'AddIns' returns object of type 'AddIns'
		"AddIns": (2003, 2, (9, 0), (), "AddIns", '{91493460-5A91-11CF-8700-00AA0060263B}'),
		# Method 'AnswerWizard' returns object of type 'AnswerWizard'
		"AnswerWizard": (2011, 2, (9, 0), (), "AnswerWizard", '{000C0360-0000-0000-C000-000000000046}'),
		# Method 'Application' returns object of type 'Application'
		"Application": (2004, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Assistant' returns object of type 'Assistant'
		"Assistant": (2005, 2, (9, 0), (), "Assistant", '{000C0322-0000-0000-C000-000000000046}'),
		# Method 'CommandBars' returns object of type 'CommandBars'
		"CommandBars": (2010, 2, (13, 0), (), "CommandBars", '{55F88893-7708-11D1-ACEB-006008961DA5}'),
		"Dialogs": (2006, 2, (13, 0), (), "Dialogs", None),
		# Method 'Presentations' returns object of type 'Presentations'
		"Presentations": (2007, 2, (9, 0), (), "Presentations", '{91493462-5A91-11CF-8700-00AA0060263B}'),
		# Method 'SlideShowWindows' returns object of type 'SlideShowWindows'
		"SlideShowWindows": (2008, 2, (9, 0), (), "SlideShowWindows", '{91493456-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Windows' returns object of type 'DocumentWindows'
		"Windows": (2009, 2, (9, 0), (), "Windows", '{91493455-5A91-11CF-8700-00AA0060263B}'),
	}
	_prop_map_put_ = {
	}

class _Master(DispatchBaseClass):
	CLSID = IID('{9149346C-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = IID('{91493447-5A91-11CF-8700-00AA0060263B}')

	def Delete(self):
		return self._oleobj_.InvokeTypes(2008, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Background' returns object of type 'ShapeRange'
		"Background": (2006, 2, (9, 0), (), "Background", '{9149347A-5A91-11CF-8700-00AA0060263B}'),
		# Method 'ColorScheme' returns object of type 'ColorScheme'
		"ColorScheme": (2005, 2, (9, 0), (), "ColorScheme", '{9149346F-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Design' returns object of type 'Design'
		"Design": (2014, 2, (9, 0), (), "Design", '{914934D7-5A91-11CF-8700-00AA0060263B}'),
		# Method 'HeadersFooters' returns object of type 'HeadersFooters'
		"HeadersFooters": (2004, 2, (9, 0), (), "HeadersFooters", '{91493474-5A91-11CF-8700-00AA0060263B}'),
		"Height": (2009, 2, (4, 0), (), "Height", None),
		# Method 'Hyperlinks' returns object of type 'Hyperlinks'
		"Hyperlinks": (2012, 2, (9, 0), (), "Hyperlinks", '{91493464-5A91-11CF-8700-00AA0060263B}'),
		"Name": (2007, 2, (8, 0), (), "Name", None),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		# Method 'Scripts' returns object of type 'Scripts'
		"Scripts": (2013, 2, (9, 0), (), "Scripts", '{000C0340-0000-0000-C000-000000000046}'),
		# Method 'Shapes' returns object of type 'Shapes'
		"Shapes": (2003, 2, (9, 0), (), "Shapes", '{91493475-5A91-11CF-8700-00AA0060263B}'),
		# Method 'SlideShowTransition' returns object of type 'SlideShowTransition'
		"SlideShowTransition": (2016, 2, (9, 0), (), "SlideShowTransition", '{91493471-5A91-11CF-8700-00AA0060263B}'),
		# Method 'TextStyles' returns object of type 'TextStyles'
		"TextStyles": (2011, 2, (9, 0), (), "TextStyles", '{91493498-5A91-11CF-8700-00AA0060263B}'),
		# Method 'TimeLine' returns object of type 'TimeLine'
		"TimeLine": (2015, 2, (9, 0), (), "TimeLine", '{914934DC-5A91-11CF-8700-00AA0060263B}'),
		"Width": (2010, 2, (4, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"ColorScheme": ((2005, LCID, 4, 0),()),
		"Name": ((2007, LCID, 4, 0),()),
	}

class _PowerRex(DispatchBaseClass):
	CLSID = IID('{914934D3-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = IID('{91493448-5A91-11CF-8700-00AA0060263B}')

	def OnAsfEncoderEvent(self, erorCode=defaultNamedNotOptArg, bstrErrorDesc=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2001, LCID, 1, (24, 0), ((12, 1), (12, 1)),erorCode
			, bstrErrorDesc)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}

class _Presentation(DispatchBaseClass):
	CLSID = IID('{9149349D-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = IID('{91493444-5A91-11CF-8700-00AA0060263B}')

	def AddBaseline(self, FileName=''):
		return self._ApplyTypes_(2073, 1, (24, 32), ((8, 49),), 'AddBaseline', None,FileName
			)

	# Result is of type _Master
	def AddTitleMaster(self):
		ret = self._oleobj_.InvokeTypes(2006, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'AddTitleMaster', '{9149346C-5A91-11CF-8700-00AA0060263B}')
		return ret

	def AddToFavorites(self):
		return self._oleobj_.InvokeTypes(2031, LCID, 1, (24, 0), (),)

	def ApplyTemplate(self, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2007, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def CanCheckIn(self):
		return self._oleobj_.InvokeTypes(2066, LCID, 1, (11, 0), (),)

	def CheckIn(self, SaveChanges=True, Comments=defaultNamedOptArg, MakePublic=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(2065, LCID, 1, (24, 0), ((11, 49), (12, 17), (12, 17)),SaveChanges
			, Comments, MakePublic)

	def Close(self):
		return self._oleobj_.InvokeTypes(2039, LCID, 1, (24, 0), (),)

	def EndReview(self):
		return self._oleobj_.InvokeTypes(2071, LCID, 1, (24, 0), (),)

	def Export(self, Path=defaultNamedNotOptArg, FilterName=defaultNamedNotOptArg, ScaleWidth=0, ScaleHeight=0):
		return self._oleobj_.InvokeTypes(2038, LCID, 1, (24, 0), ((8, 1), (8, 1), (3, 49), (3, 49)),Path
			, FilterName, ScaleWidth, ScaleHeight)

	def FollowHyperlink(self, Address=defaultNamedNotOptArg, SubAddress='', NewWindow=False, AddHistory=True
			, ExtraInfo='', Method=0, HeaderInfo=''):
		return self._ApplyTypes_(2030, 1, (24, 32), ((8, 1), (8, 49), (11, 49), (11, 49), (8, 49), (3, 49), (8, 49)), 'FollowHyperlink', None,Address
			, SubAddress, NewWindow, AddHistory, ExtraInfo, Method
			, HeaderInfo)

	def MakeIntoTemplate(self, IsDesignTemplate=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2056, LCID, 1, (24, 0), ((3, 1),),IsDesignTemplate
			)

	def Merge(self, Path=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2064, LCID, 1, (24, 0), ((8, 1),),Path
			)

	# Result is of type DocumentWindow
	def NewWindow(self):
		ret = self._oleobj_.InvokeTypes(2029, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'NewWindow', '{91493457-5A91-11CF-8700-00AA0060263B}')
		return ret

	def PrintOut(self, From=-1, To=-1, PrintToFile='', Copies=0
			, Collate=-99):
		return self._ApplyTypes_(2034, 1, (24, 32), ((3, 49), (3, 49), (8, 49), (3, 49), (3, 49)), 'PrintOut', None,From
			, To, PrintToFile, Copies, Collate)

	def ReloadAs(self, cp=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2055, LCID, 1, (24, 0), ((3, 1),),cp
			)

	def RemoveBaseline(self):
		return self._oleobj_.InvokeTypes(2074, LCID, 1, (24, 0), (),)

	def ReplyWithChanges(self, ShowMessage=True):
		return self._oleobj_.InvokeTypes(2070, LCID, 1, (24, 0), ((11, 49),),ShowMessage
			)

	def Save(self):
		return self._oleobj_.InvokeTypes(2035, LCID, 1, (24, 0), (),)

	def SaveAs(self, FileName=defaultNamedNotOptArg, FileFormat=1, EmbedTrueTypeFonts=-2):
		return self._oleobj_.InvokeTypes(2036, LCID, 1, (24, 0), ((8, 1), (3, 49), (3, 49)),FileName
			, FileFormat, EmbedTrueTypeFonts)

	def SaveCopyAs(self, FileName=defaultNamedNotOptArg, FileFormat=11, EmbedTrueTypeFonts=-2):
		return self._oleobj_.InvokeTypes(2037, LCID, 1, (24, 0), ((8, 1), (3, 49), (3, 49)),FileName
			, FileFormat, EmbedTrueTypeFonts)

	def SendFaxOverInternet(self, Recipients='', Subject='', ShowMessage=False):
		return self._ApplyTypes_(2085, 1, (24, 32), ((8, 49), (8, 49), (11, 49)), 'SendFaxOverInternet', None,Recipients
			, Subject, ShowMessage)

	def SendForReview(self, Recipients='', Subject='', ShowMessage=True, IncludeAttachment=defaultNamedOptArg):
		return self._ApplyTypes_(2069, 1, (24, 32), ((8, 49), (8, 49), (11, 49), (12, 17)), 'SendForReview', None,Recipients
			, Subject, ShowMessage, IncludeAttachment)

	def SetPasswordEncryptionOptions(self, PasswordEncryptionProvider=defaultNamedNotOptArg, PasswordEncryptionAlgorithm=defaultNamedNotOptArg, PasswordEncryptionKeyLength=defaultNamedNotOptArg, PasswordEncryptionFileProperties=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2079, LCID, 1, (24, 0), ((8, 1), (8, 1), (3, 1), (11, 1)),PasswordEncryptionProvider
			, PasswordEncryptionAlgorithm, PasswordEncryptionKeyLength, PasswordEncryptionFileProperties)

	def SetUndoText(self, Text=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2040, LCID, 1, (24, 0), ((8, 1),),Text
			)

	def UpdateLinks(self):
		return self._oleobj_.InvokeTypes(2046, LCID, 1, (24, 0), (),)

	def WebPagePreview(self):
		return self._oleobj_.InvokeTypes(2049, LCID, 1, (24, 0), (),)

	def sblt(self, s=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2058, LCID, 1, (24, 0), ((8, 1),),s
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		"BuiltInDocumentProperties": (2020, 2, (9, 0), (), "BuiltInDocumentProperties", None),
		# Method 'ColorSchemes' returns object of type 'ColorSchemes'
		"ColorSchemes": (2013, 2, (9, 0), (), "ColorSchemes", '{9149346E-5A91-11CF-8700-00AA0060263B}'),
		# Method 'CommandBars' returns object of type 'CommandBars'
		"CommandBars": (2051, 2, (13, 0), (), "CommandBars", '{55F88893-7708-11D1-ACEB-006008961DA5}'),
		"Container": (2041, 2, (9, 0), (), "Container", None),
		"CustomDocumentProperties": (2021, 2, (9, 0), (), "CustomDocumentProperties", None),
		"DefaultLanguageID": (2050, 2, (3, 0), (), "DefaultLanguageID", None),
		# Method 'DefaultShape' returns object of type 'Shape'
		"DefaultShape": (2019, 2, (9, 0), (), "DefaultShape", '{91493479-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Designs' returns object of type 'Designs'
		"Designs": (2063, 2, (9, 0), (), "Designs", '{914934D6-5A91-11CF-8700-00AA0060263B}'),
		"DisplayComments": (2042, 2, (3, 0), (), "DisplayComments", None),
		# Method 'DocumentLibraryVersions' returns object of type 'DocumentLibraryVersions'
		"DocumentLibraryVersions": (2086, 2, (9, 0), (), "DocumentLibraryVersions", '{000C0388-0000-0000-C000-000000000046}'),
		"EnvelopeVisible": (2057, 2, (3, 0), (), "EnvelopeVisible", None),
		# Method 'ExtraColors' returns object of type 'ExtraColors'
		"ExtraColors": (2014, 2, (9, 0), (), "ExtraColors", '{91493468-5A91-11CF-8700-00AA0060263B}'),
		"FarEastLineBreakLanguage": (2048, 2, (3, 0), (), "FarEastLineBreakLanguage", None),
		"FarEastLineBreakLevel": (2043, 2, (3, 0), (), "FarEastLineBreakLevel", None),
		# Method 'Fonts' returns object of type 'Fonts'
		"Fonts": (2016, 2, (9, 0), (), "Fonts", '{91493467-5A91-11CF-8700-00AA0060263B}'),
		"FullName": (2024, 2, (8, 0), (), "FullName", None),
		"GridDistance": (2062, 2, (4, 0), (), "GridDistance", None),
		# Method 'HTMLProject' returns object of type 'HTMLProject'
		"HTMLProject": (2054, 2, (9, 0), (), "HTMLProject", '{000C0356-0000-0000-C000-000000000046}'),
		# Method 'HandoutMaster' returns object of type '_Master'
		"HandoutMaster": (2010, 2, (9, 0), (), "HandoutMaster", '{9149346C-5A91-11CF-8700-00AA0060263B}'),
		"HasRevisionInfo": (2072, 2, (3, 0), (), "HasRevisionInfo", None),
		"HasTitleMaster": (2005, 2, (3, 0), (), "HasTitleMaster", None),
		"LayoutDirection": (2028, 2, (3, 0), (), "LayoutDirection", None),
		"Name": (2025, 2, (8, 0), (), "Name", None),
		"NoLineBreakAfter": (2045, 2, (8, 0), (), "NoLineBreakAfter", None),
		"NoLineBreakBefore": (2044, 2, (8, 0), (), "NoLineBreakBefore", None),
		# Method 'NotesMaster' returns object of type '_Master'
		"NotesMaster": (2009, 2, (9, 0), (), "NotesMaster", '{9149346C-5A91-11CF-8700-00AA0060263B}'),
		# Method 'PageSetup' returns object of type 'PageSetup'
		"PageSetup": (2012, 2, (9, 0), (), "PageSetup", '{91493466-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"Password": (2080, 2, (8, 0), (), "Password", None),
		"PasswordEncryptionAlgorithm": (2076, 2, (8, 0), (), "PasswordEncryptionAlgorithm", None),
		"PasswordEncryptionFileProperties": (2078, 2, (11, 0), (), "PasswordEncryptionFileProperties", None),
		"PasswordEncryptionKeyLength": (2077, 2, (3, 0), (), "PasswordEncryptionKeyLength", None),
		"PasswordEncryptionProvider": (2075, 2, (8, 0), (), "PasswordEncryptionProvider", None),
		"Path": (2026, 2, (8, 0), (), "Path", None),
		# Method 'Permission' returns object of type 'Permission'
		"Permission": (2082, 2, (9, 0), (), "Permission", '{000C0376-0000-0000-C000-000000000046}'),
		# Method 'PrintOptions' returns object of type 'PrintOptions'
		"PrintOptions": (2033, 2, (9, 0), (), "PrintOptions", '{9149345D-5A91-11CF-8700-00AA0060263B}'),
		# Method 'PublishObjects' returns object of type 'PublishObjects'
		"PublishObjects": (2052, 2, (9, 0), (), "PublishObjects", '{914934CF-5A91-11CF-8700-00AA0060263B}'),
		"ReadOnly": (2023, 2, (3, 0), (), "ReadOnly", None),
		"RemovePersonalInformation": (2068, 2, (3, 0), (), "RemovePersonalInformation", None),
		"Saved": (2027, 2, (3, 0), (), "Saved", None),
		# Method 'SharedWorkspace' returns object of type 'SharedWorkspace'
		"SharedWorkspace": (2083, 2, (9, 0), (), "SharedWorkspace", '{000C0385-0000-0000-C000-000000000046}'),
		# Method 'Signatures' returns object of type 'SignatureSet'
		"Signatures": (2067, 2, (9, 0), (), "Signatures", '{000C0410-0000-0000-C000-000000000046}'),
		# Method 'SlideMaster' returns object of type '_Master'
		"SlideMaster": (2003, 2, (9, 0), (), "SlideMaster", '{9149346C-5A91-11CF-8700-00AA0060263B}'),
		# Method 'SlideShowSettings' returns object of type 'SlideShowSettings'
		"SlideShowSettings": (2015, 2, (9, 0), (), "SlideShowSettings", '{9149345A-5A91-11CF-8700-00AA0060263B}'),
		# Method 'SlideShowWindow' returns object of type 'SlideShowWindow'
		"SlideShowWindow": (2047, 2, (9, 0), (), "SlideShowWindow", '{91493453-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Slides' returns object of type 'Slides'
		"Slides": (2011, 2, (9, 0), (), "Slides", '{91493469-5A91-11CF-8700-00AA0060263B}'),
		"SnapToGrid": (2061, 2, (3, 0), (), "SnapToGrid", None),
		# Method 'Sync' returns object of type 'Sync'
		"Sync": (2084, 2, (9, 0), (), "Sync", '{000C0386-0000-0000-C000-000000000046}'),
		# Method 'Tags' returns object of type 'Tags'
		"Tags": (2018, 2, (9, 0), (), "Tags", '{914934B9-5A91-11CF-8700-00AA0060263B}'),
		"TemplateName": (2008, 2, (8, 0), (), "TemplateName", None),
		# Method 'TitleMaster' returns object of type '_Master'
		"TitleMaster": (2004, 2, (9, 0), (), "TitleMaster", '{9149346C-5A91-11CF-8700-00AA0060263B}'),
		"VBASigned": (2059, 2, (3, 0), (), "VBASigned", None),
		# Method 'VBProject' returns object of type 'VBProject'
		"VBProject": (2022, 2, (13, 0), (), "VBProject", '{0002E169-0000-0000-C000-000000000046}'),
		# Method 'WebOptions' returns object of type 'WebOptions'
		"WebOptions": (2053, 2, (9, 0), (), "WebOptions", '{914934CE-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Windows' returns object of type 'DocumentWindows'
		"Windows": (2017, 2, (9, 0), (), "Windows", '{91493455-5A91-11CF-8700-00AA0060263B}'),
		"WritePassword": (2081, 2, (8, 0), (), "WritePassword", None),
	}
	_prop_map_put_ = {
		"DefaultLanguageID": ((2050, LCID, 4, 0),()),
		"DisplayComments": ((2042, LCID, 4, 0),()),
		"EnvelopeVisible": ((2057, LCID, 4, 0),()),
		"FarEastLineBreakLanguage": ((2048, LCID, 4, 0),()),
		"FarEastLineBreakLevel": ((2043, LCID, 4, 0),()),
		"GridDistance": ((2062, LCID, 4, 0),()),
		"LayoutDirection": ((2028, LCID, 4, 0),()),
		"NoLineBreakAfter": ((2045, LCID, 4, 0),()),
		"NoLineBreakBefore": ((2044, LCID, 4, 0),()),
		"Password": ((2080, LCID, 4, 0),()),
		"RemovePersonalInformation": ((2068, LCID, 4, 0),()),
		"Saved": ((2027, LCID, 4, 0),()),
		"SnapToGrid": ((2061, LCID, 4, 0),()),
		"WritePassword": ((2081, LCID, 4, 0),()),
	}

class _Slide(DispatchBaseClass):
	CLSID = IID('{9149346A-5A91-11CF-8700-00AA0060263B}')
	coclass_clsid = IID('{91493445-5A91-11CF-8700-00AA0060263B}')

	def ApplyTemplate(self, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2032, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def Copy(self):
		return self._oleobj_.InvokeTypes(2013, LCID, 1, (24, 0), (),)

	def Cut(self):
		return self._oleobj_.InvokeTypes(2012, LCID, 1, (24, 0), (),)

	def Delete(self):
		return self._oleobj_.InvokeTypes(2016, LCID, 1, (24, 0), (),)

	# Result is of type SlideRange
	def Duplicate(self):
		ret = self._oleobj_.InvokeTypes(2015, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', '{9149346B-5A91-11CF-8700-00AA0060263B}')
		return ret

	def Export(self, FileName=defaultNamedNotOptArg, FilterName=defaultNamedNotOptArg, ScaleWidth=0, ScaleHeight=0):
		return self._oleobj_.InvokeTypes(2025, LCID, 1, (24, 0), ((8, 1), (8, 1), (3, 49), (3, 49)),FileName
			, FilterName, ScaleWidth, ScaleHeight)

	def MoveTo(self, toPos=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2030, LCID, 1, (24, 0), ((3, 1),),toPos
			)

	def Select(self):
		return self._oleobj_.InvokeTypes(2011, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2001, 2, (13, 0), (), "Application", '{91493441-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Background' returns object of type 'ShapeRange'
		"Background": (2007, 2, (9, 0), (), "Background", '{9149347A-5A91-11CF-8700-00AA0060263B}'),
		# Method 'ColorScheme' returns object of type 'ColorScheme'
		"ColorScheme": (2006, 2, (9, 0), (), "ColorScheme", '{9149346F-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Comments' returns object of type 'Comments'
		"Comments": (2028, 2, (9, 0), (), "Comments", '{914934D4-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Design' returns object of type 'Design'
		"Design": (2029, 2, (9, 0), (), "Design", '{914934D7-5A91-11CF-8700-00AA0060263B}'),
		"DisplayMasterShapes": (2020, 2, (3, 0), (), "DisplayMasterShapes", None),
		"FollowMasterBackground": (2021, 2, (3, 0), (), "FollowMasterBackground", None),
		# Method 'HeadersFooters' returns object of type 'HeadersFooters'
		"HeadersFooters": (2004, 2, (9, 0), (), "HeadersFooters", '{91493474-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Hyperlinks' returns object of type 'Hyperlinks'
		"Hyperlinks": (2024, 2, (9, 0), (), "Hyperlinks", '{91493464-5A91-11CF-8700-00AA0060263B}'),
		"Layout": (2014, 2, (3, 0), (), "Layout", None),
		# Method 'Master' returns object of type '_Master'
		"Master": (2023, 2, (9, 0), (), "Master", '{9149346C-5A91-11CF-8700-00AA0060263B}'),
		"Name": (2008, 2, (8, 0), (), "Name", None),
		# Method 'NotesPage' returns object of type 'SlideRange'
		"NotesPage": (2022, 2, (9, 0), (), "NotesPage", '{9149346B-5A91-11CF-8700-00AA0060263B}'),
		"Parent": (2002, 2, (9, 0), (), "Parent", None),
		"PrintSteps": (2010, 2, (3, 0), (), "PrintSteps", None),
		# Method 'Scripts' returns object of type 'Scripts'
		"Scripts": (2026, 2, (9, 0), (), "Scripts", '{000C0340-0000-0000-C000-000000000046}'),
		# Method 'Shapes' returns object of type 'Shapes'
		"Shapes": (2003, 2, (9, 0), (), "Shapes", '{91493475-5A91-11CF-8700-00AA0060263B}'),
		"SlideID": (2009, 2, (3, 0), (), "SlideID", None),
		"SlideIndex": (2018, 2, (3, 0), (), "SlideIndex", None),
		"SlideNumber": (2019, 2, (3, 0), (), "SlideNumber", None),
		# Method 'SlideShowTransition' returns object of type 'SlideShowTransition'
		"SlideShowTransition": (2005, 2, (9, 0), (), "SlideShowTransition", '{91493471-5A91-11CF-8700-00AA0060263B}'),
		# Method 'Tags' returns object of type 'Tags'
		"Tags": (2017, 2, (9, 0), (), "Tags", '{914934B9-5A91-11CF-8700-00AA0060263B}'),
		# Method 'TimeLine' returns object of type 'TimeLine'
		"TimeLine": (2031, 2, (9, 0), (), "TimeLine", '{914934DC-5A91-11CF-8700-00AA0060263B}'),
	}
	_prop_map_put_ = {
		"ColorScheme": ((2006, LCID, 4, 0),()),
		"Design": ((2029, LCID, 4, 0),()),
		"DisplayMasterShapes": ((2020, LCID, 4, 0),()),
		"FollowMasterBackground": ((2021, LCID, 4, 0),()),
		"Layout": ((2014, LCID, 4, 0),()),
		"Name": ((2008, LCID, 4, 0),()),
	}

from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'PowerPoint.Application.11'
class Application(CoClassBaseClass): # A CoClass
	CLSID = IID('{91493441-5A91-11CF-8700-00AA0060263B}')
	coclass_sources = [
		EApplication,
	]
	default_source = EApplication
	coclass_interfaces = [
		_Application,
	]
	default_interface = _Application

class Global(CoClassBaseClass): # A CoClass
	CLSID = IID('{91493443-5A91-11CF-8700-00AA0060263B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Global,
	]
	default_interface = _Global

class Master(CoClassBaseClass): # A CoClass
	CLSID = IID('{91493447-5A91-11CF-8700-00AA0060263B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Master,
	]
	default_interface = _Master

class OLEControl(CoClassBaseClass): # A CoClass
	CLSID = IID('{91493446-5A91-11CF-8700-00AA0060263B}')
	coclass_sources = [
		OCXExtenderEvents,
	]
	default_source = OCXExtenderEvents
	coclass_interfaces = [
		OCXExtender,
	]
	default_interface = OCXExtender

class PowerRex(CoClassBaseClass): # A CoClass
	CLSID = IID('{91493448-5A91-11CF-8700-00AA0060263B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PowerRex,
	]
	default_interface = _PowerRex

class Presentation(CoClassBaseClass): # A CoClass
	CLSID = IID('{91493444-5A91-11CF-8700-00AA0060263B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Presentation,
	]
	default_interface = _Presentation

class Slide(CoClassBaseClass): # A CoClass
	CLSID = IID('{91493445-5A91-11CF-8700-00AA0060263B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Slide,
	]
	default_interface = _Slide

ActionSetting_vtables_dispatch_ = 1
ActionSetting_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Action' , 'Action' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Action' , 'Action' , ), 2003, (2003, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'ActionVerb' , 'ActionVerb' , ), 2004, (2004, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'ActionVerb' , 'ActionVerb' , ), 2004, (2004, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'AnimateAction' , 'AnimateAction' , ), 2005, (2005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'AnimateAction' , 'AnimateAction' , ), 2005, (2005, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Run' , 'Run' , ), 2006, (2006, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'Run' , 'Run' , ), 2006, (2006, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SlideShowName' , 'SlideShowName' , ), 2007, (2007, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'SlideShowName' , 'SlideShowName' , ), 2007, (2007, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Hyperlink' , 'Hyperlink' , ), 2008, (2008, (), [ (16393, 10, None, "IID('{91493465-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'SoundEffect' , 'SoundEffect' , ), 2009, (2009, (), [ (16393, 10, None, "IID('{91493472-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ShowAndReturn' , 'ShowAndReturn' , ), 2010, (2010, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'ShowAndReturn' , 'ShowAndReturn' , ), 2010, (2010, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ActionSettings_vtables_dispatch_ = 1
ActionSettings_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{9149348D-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

AddIn_vtables_dispatch_ = 1
AddIn_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'FullName' , 'FullName' , ), 2003, (2003, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 2004, (2004, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Path' , 'Path' , ), 2005, (2005, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Registered' , 'Registered' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Registered' , 'Registered' , ), 2006, (2006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'AutoLoad' , 'AutoLoad' , ), 2007, (2007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'AutoLoad' , 'AutoLoad' , ), 2007, (2007, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'Loaded' , 'Loaded' , ), 2008, (2008, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Loaded' , 'Loaded' , ), 2008, (2008, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'DisplayAlerts' , 'DisplayAlerts' , ), 2009, (2009, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 64 , )),
	(( 'DisplayAlerts' , 'DisplayAlerts' , ), 2009, (2009, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 64 , )),
	(( 'RegisteredInHKLM' , 'RegisteredInHKLM' , ), 2010, (2010, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 64 , )),
]

AddIns_vtables_dispatch_ = 1
AddIns_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (16396, 1, None, None) , 
			(16393, 10, None, "IID('{91493461-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'FileName' , 'Add' , ), 2003, (2003, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{91493461-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Index' , ), 2004, (2004, (), [ (16396, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

Adjustments_vtables_dispatch_ = 1
Adjustments_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Val' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Val' , ), 0, (0, (), [ (3, 1, None, None) , 
			(4, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

AnimationBehavior_vtables_dispatch_ = 1
AnimationBehavior_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Additive' , 'Additive' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Additive' , 'Additive' , ), 2003, (2003, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Accumulate' , 'Accumulate' , ), 2004, (2004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Accumulate' , 'Accumulate' , ), 2004, (2004, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 2005, (2005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 2005, (2005, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MotionEffect' , 'MotionEffect' , ), 2006, (2006, (), [ (16393, 10, None, "IID('{914934E5-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'ColorEffect' , 'ColorEffect' , ), 2007, (2007, (), [ (16393, 10, None, "IID('{914934E6-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ScaleEffect' , 'ScaleEffect' , ), 2008, (2008, (), [ (16393, 10, None, "IID('{914934E7-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'RotationEffect' , 'RotationEffect' , ), 2009, (2009, (), [ (16393, 10, None, "IID('{914934E8-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'PropertyEffect' , 'PropertyEffect' , ), 2010, (2010, (), [ (16393, 10, None, "IID('{914934E9-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'Timing' , 'Timing' , ), 2011, (2011, (), [ (16393, 10, None, "IID('{914934E0-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 2012, (2012, (), [ ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'CommandEffect' , 'CommandEffect' , ), 2013, (2013, (), [ (16393, 10, None, "IID('{914934EF-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'FilterEffect' , 'FilterEffect' , ), 2014, (2014, (), [ (16393, 10, None, "IID('{914934F0-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'SetEffect' , 'SetEffect' , ), 2015, (2015, (), [ (16393, 10, None, "IID('{914934F1-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

AnimationBehaviors_vtables_dispatch_ = 1
AnimationBehaviors_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{914934E4-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Type' , 'Index' , 'Add' , ), 2003, (2003, (), [ 
			(3, 1, None, None) , (3, 49, '-1', None) , (16393, 10, None, "IID('{914934E4-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

AnimationPoint_vtables_dispatch_ = 1
AnimationPoint_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 2003, (2003, (), [ ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Time' , 'Time' , ), 2004, (2004, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Time' , 'Time' , ), 2004, (2004, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'Value' , ), 2005, (2005, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'Value' , ), 2005, (2005, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Formula' , 'Formula' , ), 2006, (2006, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Formula' , 'Formula' , ), 2006, (2006, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
]

AnimationPoints_vtables_dispatch_ = 1
AnimationPoints_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{914934EB-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Index' , 'Add' , ), 2003, (2003, (), [ (3, 49, '-1', None) , 
			(16393, 10, None, "IID('{914934EB-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Smooth' , 'Smooth' , ), 2004, (2004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Smooth' , 'Smooth' , ), 2004, (2004, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
]

AnimationSettings_vtables_dispatch_ = 1
AnimationSettings_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'DimColor' , 'DimColor' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{91493452-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'SoundEffect' , 'SoundEffect' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{91493472-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'EntryEffect' , 'EntryEffect' , ), 2005, (2005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'EntryEffect' , 'EntryEffect' , ), 2005, (2005, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'AfterEffect' , 'AfterEffect' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'AfterEffect' , 'AfterEffect' , ), 2006, (2006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'AnimationOrder' , 'AnimationOrder' , ), 2007, (2007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'AnimationOrder' , 'AnimationOrder' , ), 2007, (2007, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'AdvanceMode' , 'AdvanceMode' , ), 2008, (2008, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'AdvanceMode' , 'AdvanceMode' , ), 2008, (2008, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'AdvanceTime' , 'AdvanceTime' , ), 2009, (2009, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'AdvanceTime' , 'AdvanceTime' , ), 2009, (2009, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'PlaySettings' , 'PlaySettings' , ), 2010, (2010, (), [ (16393, 10, None, "IID('{9149348E-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'TextLevelEffect' , 'TextLevelEffect' , ), 2011, (2011, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'TextLevelEffect' , 'TextLevelEffect' , ), 2011, (2011, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'TextUnitEffect' , 'TextUnitEffect' , ), 2012, (2012, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'TextUnitEffect' , 'TextUnitEffect' , ), 2012, (2012, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'Animate' , 'Animate' , ), 2013, (2013, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Animate' , 'Animate' , ), 2013, (2013, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'AnimateBackground' , 'AnimateBackground' , ), 2014, (2014, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'AnimateBackground' , 'AnimateBackground' , ), 2014, (2014, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'AnimateTextInReverse' , 'AnimateTextInReverse' , ), 2015, (2015, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'AnimateTextInReverse' , 'AnimateTextInReverse' , ), 2015, (2015, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'ChartUnitEffect' , 'ChartUnitEffect' , ), 2016, (2016, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ChartUnitEffect' , 'ChartUnitEffect' , ), 2016, (2016, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
]

AutoCorrect_vtables_dispatch_ = 1
AutoCorrect_vtables_ = [
	(( 'DisplayAutoCorrectOptions' , 'DisplayAutoCorrectOptions' , ), 2001, (2001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'DisplayAutoCorrectOptions' , 'DisplayAutoCorrectOptions' , ), 2001, (2001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'DisplayAutoLayoutOptions' , 'DisplayAutoLayoutOptions' , ), 2002, (2002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'DisplayAutoLayoutOptions' , 'DisplayAutoLayoutOptions' , ), 2002, (2002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
]

Borders_vtables_dispatch_ = 1
Borders_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'BorderType' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{9149347F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

BulletFormat_vtables_dispatch_ = 1
BulletFormat_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'Visible' , ), 0, (0, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 64 , )),
	(( 'Visible' , 'Visible' , ), 0, (0, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 64 , )),
	(( 'Character' , 'Character' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Character' , 'Character' , ), 2003, (2003, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'RelativeSize' , 'RelativeSize' , ), 2004, (2004, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'RelativeSize' , 'RelativeSize' , ), 2004, (2004, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseTextColor' , 'UseTextColor' , ), 2005, (2005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'UseTextColor' , 'UseTextColor' , ), 2005, (2005, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseTextFont' , 'UseTextFont' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'UseTextFont' , 'UseTextFont' , ), 2006, (2006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Font' , 'Font' , ), 2007, (2007, (), [ (16393, 10, None, "IID('{91493495-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 2008, (2008, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 2008, (2008, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'Style' , 'Style' , ), 2009, (2009, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Style' , 'Style' , ), 2009, (2009, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'StartValue' , 'StartValue' , ), 2010, (2010, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'StartValue' , 'StartValue' , ), 2010, (2010, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'Picture' , 'Picture' , ), 2011, (2011, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Number' , 'Number' , ), 2012, (2012, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
]

CalloutFormat_vtables_dispatch_ = 1
CalloutFormat_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'AutomaticLength' , ), 10, (10, (), [ ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'CustomDrop' , 'Drop' , ), 11, (11, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'CustomLength' , 'Length' , ), 12, (12, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'PresetDrop' , 'DropType' , ), 13, (13, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Accent' , 'Accent' , ), 100, (100, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Accent' , 'Accent' , ), 100, (100, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'Angle' , 'Angle' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Angle' , 'Angle' , ), 101, (101, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'AutoAttach' , 'AutoAttach' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'AutoAttach' , 'AutoAttach' , ), 102, (102, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'AutoLength' , 'AutoLength' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Border' , 'Border' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'Border' , 'Border' , ), 104, (104, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Drop' , 'Drop' , ), 105, (105, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'DropType' , 'DropType' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Gap' , 'Gap' , ), 107, (107, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'Gap' , 'Gap' , ), 107, (107, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Length' , 'Length' , ), 108, (108, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 109, (109, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 109, (109, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
]

CanvasShapes_vtables_dispatch_ = 1
CanvasShapes_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			(16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , '_NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 1024 , )),
	(( 'AddCallout' , 'Type' , 'Left' , 'Top' , 'Width' , 
			'Height' , 'Callout' , ), 10, (10, (), [ (3, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'AddConnector' , 'Type' , 'BeginX' , 'BeginY' , 'EndX' , 
			'EndY' , 'Connector' , ), 11, (11, (), [ (3, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'AddCurve' , 'SafeArrayOfPoints' , 'Curve' , ), 12, (12, (), [ (12, 1, None, None) , 
			(16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'AddLabel' , 'Orientation' , 'Left' , 'Top' , 'Width' , 
			'Height' , 'Label' , ), 13, (13, (), [ (3, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'AddLine' , 'BeginX' , 'BeginY' , 'EndX' , 'EndY' , 
			'Line' , ), 14, (14, (), [ (4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'AddPicture' , 'FileName' , 'LinkToFile' , 'SaveWithDocument' , 'Left' , 
			'Top' , 'Width' , 'Height' , 'Picture' , ), 15, (15, (), [ 
			(8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , 
			(4, 49, '-1.0', None) , (4, 49, '-1.0', None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'AddPolyline' , 'SafeArrayOfPoints' , 'Polyline' , ), 16, (16, (), [ (12, 1, None, None) , 
			(16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'AddShape' , 'Type' , 'Left' , 'Top' , 'Width' , 
			'Height' , 'Shape' , ), 17, (17, (), [ (3, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'AddTextEffect' , 'PresetTextEffect' , 'Text' , 'FontName' , 'FontSize' , 
			'FontBold' , 'FontItalic' , 'Left' , 'Top' , 'TextEffect' , 
			), 18, (18, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (4, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'AddTextbox' , 'Orientation' , 'Left' , 'Top' , 'Width' , 
			'Height' , 'Textbox' , ), 19, (19, (), [ (3, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'BuildFreeform' , 'EditingType' , 'X1' , 'Y1' , 'FreeformBuilder' , 
			), 20, (20, (), [ (3, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (16393, 10, None, "IID('{91493478-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'Range' , 'Index' , 'Range' , ), 21, (21, (), [ (12, 1, None, None) , 
			(16393, 10, None, "IID('{9149347A-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'SelectAll' , ), 22, (22, (), [ ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'Background' , 'Background' , ), 100, (100, (), [ (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

Cell_vtables_dispatch_ = 1
Cell_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Shape' , 'Shape' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Borders' , 'Borders' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{914934CA-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Merge' , 'MergeTo' , ), 2005, (2005, (), [ (9, 1, None, "IID('{914934C9-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Split' , 'NumRows' , 'NumColumns' , ), 2006, (2006, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Select' , ), 2007, (2007, (), [ ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Selected' , 'Selected' , ), 2008, (2008, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

CellRange_vtables_dispatch_ = 1
CellRange_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{914934C9-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Borders' , 'Borders' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{914934CA-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

Collection_vtables_dispatch_ = 1
Collection_vtables_ = [
	(( '_NewEnum' , '_NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 1 , )),
	(( '_Index' , 'Index' , '_Index' , ), 10, (10, (), [ (3, 1, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 1 , )),
	(( 'Count' , 'Count' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
]

ColorEffect_vtables_dispatch_ = 1
ColorEffect_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'By' , 'By' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{91493452-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'From' , 'From' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{91493452-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'To' , 'To' , ), 2005, (2005, (), [ (16393, 10, None, "IID('{91493452-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
]

ColorFormat_vtables_dispatch_ = 1
ColorFormat_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'RGB' , 'RGB' , ), 0, (0, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'RGB' , 'RGB' , ), 0, (0, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'SchemeColor' , 'SchemeColor' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'SchemeColor' , 'SchemeColor' , ), 2003, (2003, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'TintAndShade' , 'pValue' , ), 103, (103, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'TintAndShade' , 'pValue' , ), 103, (103, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ColorScheme_vtables_dispatch_ = 1
ColorScheme_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Colors' , 'SchemeColor' , 'Colors' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{91493470-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 2003, (2003, (), [ ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

ColorSchemes_vtables_dispatch_ = 1
ColorSchemes_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{9149346F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Scheme' , 'Add' , ), 2003, (2003, (), [ (9, 49, '0', "IID('{9149346F-5A91-11CF-8700-00AA0060263B}')") , 
			(16393, 10, None, "IID('{9149346F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

Column_vtables_dispatch_ = 1
Column_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Cells' , 'Cells' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{914934C8-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Select' , ), 2004, (2004, (), [ ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 2005, (2005, (), [ ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 2006, (2006, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 2006, (2006, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

Columns_vtables_dispatch_ = 1
Columns_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{914934C5-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'BeforeColumn' , 'Add' , ), 2003, (2003, (), [ (3, 49, '-1', None) , 
			(16393, 10, None, "IID('{914934C5-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

CommandEffect_vtables_dispatch_ = 1
CommandEffect_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 2003, (2003, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Command' , 'Command' , ), 2004, (2004, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Command' , 'Command' , ), 2004, (2004, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

Comment_vtables_dispatch_ = 1
Comment_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Author' , 'Author' , ), 2003, (2003, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'AuthorInitials' , 'AuthorInitials' , ), 2004, (2004, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'Text' , ), 2005, (2005, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'DateTime' , 'DateTime' , ), 2006, (2006, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'AuthorIndex' , 'AuthorIndex' , ), 2007, (2007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Left' , 'Left' , ), 2008, (2008, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Top' , 'Top' , ), 2009, (2009, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 2010, (2010, (), [ ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

Comments_vtables_dispatch_ = 1
Comments_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{914934D5-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Left' , 'Top' , 'Author' , 'AuthorInitials' , 
			'Text' , 'Add' , ), 2003, (2003, (), [ (4, 1, None, None) , (4, 1, None, None) , 
			(8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{914934D5-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

ConnectorFormat_vtables_dispatch_ = 1
ConnectorFormat_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'BeginConnect' , 'ConnectedShape' , 'ConnectionSite' , ), 10, (10, (), [ (9, 1, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'BeginDisconnect' , ), 11, (11, (), [ ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'EndConnect' , 'ConnectedShape' , 'ConnectionSite' , ), 12, (12, (), [ (9, 1, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'EndDisconnect' , ), 13, (13, (), [ ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'BeginConnected' , 'BeginConnected' , ), 100, (100, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'BeginConnectedShape' , 'BeginConnectedShape' , ), 101, (101, (), [ (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'BeginConnectionSite' , 'BeginConnectionSite' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'EndConnected' , 'EndConnected' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'EndConnectedShape' , 'EndConnectedShape' , ), 104, (104, (), [ (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'EndConnectionSite' , 'EndConnectionSite' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 106, (106, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
]

DefaultWebOptions_vtables_dispatch_ = 1
DefaultWebOptions_vtables_ = [
	(( 'IncludeNavigation' , 'IncludeNavigation' , ), 2001, (2001, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'IncludeNavigation' , 'IncludeNavigation' , ), 2001, (2001, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'FrameColors' , 'FrameColors' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'FrameColors' , 'FrameColors' , ), 2002, (2002, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'ResizeGraphics' , 'ResizeGraphics' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'ResizeGraphics' , 'ResizeGraphics' , ), 2003, (2003, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'ShowSlideAnimation' , 'ShowSlideAnimation' , ), 2004, (2004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'ShowSlideAnimation' , 'ShowSlideAnimation' , ), 2004, (2004, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'OrganizeInFolder' , 'OrganizeInFolder' , ), 2005, (2005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'OrganizeInFolder' , 'OrganizeInFolder' , ), 2005, (2005, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseLongFileNames' , 'UseLongFileNames' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'UseLongFileNames' , 'UseLongFileNames' , ), 2006, (2006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'RelyOnVML' , 'RelyOnVML' , ), 2007, (2007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'RelyOnVML' , 'RelyOnVML' , ), 2007, (2007, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'AllowPNG' , 'AllowPNG' , ), 2008, (2008, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'AllowPNG' , 'AllowPNG' , ), 2008, (2008, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ScreenSize' , 'ScreenSize' , ), 2009, (2009, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'ScreenSize' , 'ScreenSize' , ), 2009, (2009, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Encoding' , 'Encoding' , ), 2010, (2010, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'Encoding' , 'Encoding' , ), 2010, (2010, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UpdateLinksOnSave' , 'UpdateLinksOnSave' , ), 2011, (2011, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'UpdateLinksOnSave' , 'UpdateLinksOnSave' , ), 2011, (2011, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'CheckIfOfficeIsHTMLEditor' , 'CheckIfOfficeIsHTMLEditor' , ), 2012, (2012, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'CheckIfOfficeIsHTMLEditor' , 'CheckIfOfficeIsHTMLEditor' , ), 2012, (2012, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'AlwaysSaveInDefaultEncoding' , 'AlwaysSaveInDefaultEncoding' , ), 2013, (2013, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'AlwaysSaveInDefaultEncoding' , 'AlwaysSaveInDefaultEncoding' , ), 2013, (2013, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Fonts' , 'Fonts' , ), 2014, (2014, (), [ (16393, 10, None, "IID('{000C0914-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'FolderSuffix' , 'FolderSuffix' , ), 2015, (2015, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'TargetBrowser' , 'TargetBrowser' , ), 2016, (2016, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'TargetBrowser' , 'TargetBrowser' , ), 2016, (2016, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'SaveNewWebPagesAsWebArchives' , 'SaveNewWebPagesAsWebArchives' , ), 2017, (2017, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( 'SaveNewWebPagesAsWebArchives' , 'SaveNewWebPagesAsWebArchives' , ), 2017, (2017, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'HTMLVersion' , 'HTMLVersion' , ), 2018, (2018, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( 'HTMLVersion' , 'HTMLVersion' , ), 2018, (2018, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

Design_vtables_dispatch_ = 1
Design_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'SlideMaster' , 'SlideMaster' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{9149346C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'TitleMaster' , 'TitleMaster' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{9149346C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'HasTitleMaster' , 'HasTitleMaster' , ), 2005, (2005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'AddTitleMaster' , 'TitleMaster' , ), 2006, (2006, (), [ (16393, 10, None, "IID('{9149346C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Index' , 'Index' , ), 2007, (2007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 2008, (2008, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 2008, (2008, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'Preserved' , 'Preserved' , ), 2009, (2009, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Preserved' , 'Preserved' , ), 2009, (2009, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'MoveTo' , 'toPos' , ), 2010, (2010, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 2011, (2011, (), [ ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
]

Designs_vtables_dispatch_ = 1
Designs_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			(16393, 10, None, "IID('{914934D7-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'designName' , 'Index' , 'Add' , ), 2003, (2003, (), [ 
			(8, 1, None, None) , (3, 49, '-1', None) , (16393, 10, None, "IID('{914934D7-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Load' , 'TemplateName' , 'Index' , 'Load' , ), 2004, (2004, (), [ 
			(8, 1, None, None) , (3, 49, '-1', None) , (16393, 10, None, "IID('{914934D7-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Clone' , 'pOriginal' , 'Index' , 'Clone' , ), 2005, (2005, (), [ 
			(9, 1, None, "IID('{914934D7-5A91-11CF-8700-00AA0060263B}')") , (3, 49, '-1', None) , (16393, 10, None, "IID('{914934D7-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
]

Diagram_vtables_dispatch_ = 1
Diagram_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 100, (100, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Nodes' , 'Nodes' , ), 101, (101, (), [ (16393, 10, None, "IID('{914934DA-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'AutoLayout' , 'AutoLayout' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'AutoLayout' , 'AutoLayout' , ), 103, (103, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Reverse' , 'Reverse' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Reverse' , 'Reverse' , ), 104, (104, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'AutoFormat' , 'AutoFormat' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'AutoFormat' , 'AutoFormat' , ), 105, (105, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'Convert' , 'Type' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FitText' , ), 11, (11, (), [ ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
]

DiagramNode_vtables_dispatch_ = 1
DiagramNode_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'AddNode' , 'Pos' , 'NodeType' , 'NewNode' , ), 10, (10, (), [ 
			(3, 49, '2', None) , (3, 49, '1', None) , (16393, 10, None, "IID('{914934D8-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 11, (11, (), [ ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'MoveNode' , 'TargetNode' , 'Pos' , ), 12, (12, (), [ (9, 1, None, "IID('{914934D8-5A91-11CF-8700-00AA0060263B}')") , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'ReplaceNode' , 'TargetNode' , ), 13, (13, (), [ (9, 1, None, "IID('{914934D8-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'SwapNode' , 'TargetNode' , 'SwapChildren' , ), 14, (14, (), [ (9, 1, None, "IID('{914934D8-5A91-11CF-8700-00AA0060263B}')") , 
			(11, 49, 'True', None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'CloneNode' , 'CopyChildren' , 'TargetNode' , 'Pos' , 'Node' , 
			), 15, (15, (), [ (11, 1, None, None) , (9, 1, None, "IID('{914934D8-5A91-11CF-8700-00AA0060263B}')") , (3, 49, '2', None) , (16393, 10, None, "IID('{914934D8-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'TransferChildren' , 'ReceivingNode' , ), 16, (16, (), [ (9, 1, None, "IID('{914934D8-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'NextNode' , 'NextNode' , ), 17, (17, (), [ (16393, 10, None, "IID('{914934D8-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'PrevNode' , 'PrevNode' , ), 18, (18, (), [ (16393, 10, None, "IID('{914934D8-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 100, (100, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Children' , 'Children' , ), 101, (101, (), [ (16393, 10, None, "IID('{914934D9-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'Shape' , 'Shape' , ), 102, (102, (), [ (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Root' , 'Root' , ), 103, (103, (), [ (16393, 10, None, "IID('{914934D8-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'Diagram' , 'Diagram' , ), 104, (104, (), [ (16393, 10, None, "IID('{914934DB-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Layout' , 'Type' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'Layout' , 'Type' , ), 105, (105, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'TextShape' , 'Shape' , ), 106, (106, (), [ (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
]

DiagramNodeChildren_vtables_dispatch_ = 1
DiagramNodeChildren_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppunkEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 1024 , )),
	(( 'Item' , 'Index' , 'Node' , ), 0, (0, (), [ (12, 1, None, None) , 
			(16393, 10, None, "IID('{914934D8-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'AddNode' , 'Index' , 'NodeType' , 'NewNode' , ), 10, (10, (), [ 
			(12, 49, '-1', None) , (3, 49, '1', None) , (16393, 10, None, "IID('{914934D8-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'SelectAll' , ), 11, (11, (), [ ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 100, (100, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'iDiagramNodes' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FirstChild' , 'First' , ), 103, (103, (), [ (16393, 10, None, "IID('{914934D8-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'LastChild' , 'Last' , ), 104, (104, (), [ (16393, 10, None, "IID('{914934D8-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

DiagramNodes_vtables_dispatch_ = 1
DiagramNodes_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppunkEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 1024 , )),
	(( 'Item' , 'Index' , 'ppdn' , ), 0, (0, (), [ (12, 1, None, None) , 
			(16393, 10, None, "IID('{914934D8-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'SelectAll' , ), 10, (10, (), [ ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 100, (100, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'iDiagramNodes' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

DocumentWindow_vtables_dispatch_ = 1
DocumentWindow_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Selection' , 'Selection' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{91493454-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'View' , 'View' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{91493458-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Presentation' , 'Presentation' , ), 2005, (2005, (), [ (16397, 10, None, "IID('{91493444-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'ViewType' , 'ViewType' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'ViewType' , 'ViewType' , ), 2006, (2006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'BlackAndWhite' , 'BlackAndWhite' , ), 2007, (2007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'BlackAndWhite' , 'BlackAndWhite' , ), 2007, (2007, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'Active' , 'Active' , ), 2008, (2008, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'WindowState' , 'WindowState' , ), 2009, (2009, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'WindowState' , 'WindowState' , ), 2009, (2009, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Caption' , 'Caption' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'Left' , 'Left' , ), 2010, (2010, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Left' , 'Left' , ), 2010, (2010, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'Top' , 'Top' , ), 2011, (2011, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Top' , 'Top' , ), 2011, (2011, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 2012, (2012, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 2012, (2012, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'Height' , ), 2013, (2013, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'Height' , ), 2013, (2013, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'FitToPage' , ), 2014, (2014, (), [ ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Activate' , ), 2015, (2015, (), [ ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'LargeScroll' , 'Down' , 'Up' , 'ToRight' , 'ToLeft' , 
			), 2016, (2016, (), [ (3, 49, '1', None) , (3, 49, '0', None) , (3, 49, '0', None) , (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SmallScroll' , 'Down' , 'Up' , 'ToRight' , 'ToLeft' , 
			), 2017, (2017, (), [ (3, 49, '1', None) , (3, 49, '0', None) , (3, 49, '0', None) , (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'NewWindow' , 'NewWindow' , ), 2018, (2018, (), [ (16393, 10, None, "IID('{91493457-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Close' , ), 2019, (2019, (), [ ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'HWND' , 'HWND' , ), 2020, (2020, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 1 , )),
	(( 'ActivePane' , 'ActivePane' , ), 2021, (2021, (), [ (16393, 10, None, "IID('{914934CC-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'Panes' , 'Panes' , ), 2022, (2022, (), [ (16393, 10, None, "IID('{914934CB-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'SplitVertical' , 'SplitVertical' , ), 2023, (2023, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( 'SplitVertical' , 'SplitVertical' , ), 2023, (2023, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'SplitHorizontal' , 'SplitHorizontal' , ), 2024, (2024, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( 'SplitHorizontal' , 'SplitHorizontal' , ), 2024, (2024, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'RangeFromPoint' , 'X' , 'Y' , 'RangeFromPoint' , ), 2025, (2025, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( 'PointsToScreenPixelsX' , 'Points' , 'PointsToScreenPixelsX' , ), 2026, (2026, (), [ (4, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'PointsToScreenPixelsY' , 'Points' , 'PointsToScreenPixelsY' , ), 2027, (2027, (), [ (4, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( 'ScrollIntoView' , 'Left' , 'Top' , 'Width' , 'Height' , 
			'Start' , ), 2028, (2028, (), [ (4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (3, 49, '-1', None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
]

DocumentWindows_vtables_dispatch_ = 1
DocumentWindows_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{91493457-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Arrange' , 'arrangeStyle' , ), 2003, (2003, (), [ (3, 49, '1', None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

Effect_vtables_dispatch_ = 1
Effect_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Shape' , 'Shape' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Shape' , 'Shape' , ), 2003, (2003, (), [ (9, 1, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'MoveTo' , 'toPos' , ), 2004, (2004, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'MoveBefore' , 'Effect' , ), 2005, (2005, (), [ (9, 1, None, "IID('{914934DF-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'MoveAfter' , 'Effect' , ), 2006, (2006, (), [ (9, 1, None, "IID('{914934DF-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 2007, (2007, (), [ ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Index' , 'Index' , ), 2008, (2008, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'Timing' , 'Timing' , ), 2009, (2009, (), [ (16393, 10, None, "IID('{914934E0-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'EffectType' , 'EffectType' , ), 2010, (2010, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'EffectType' , 'EffectType' , ), 2010, (2010, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'EffectParameters' , 'EffectParameters' , ), 2011, (2011, (), [ (16393, 10, None, "IID('{914934E1-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'TextRangeStart' , 'TextRangeStart' , ), 2012, (2012, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'TextRangeLength' , 'TextRangeLength' , ), 2013, (2013, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'Paragraph' , 'Paragraph' , ), 2014, (2014, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Paragraph' , 'Paragraph' , ), 2014, (2014, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'DisplayName' , 'DisplayName' , ), 2015, (2015, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Exit' , 'Exit' , ), 2016, (2016, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'Exit' , 'Exit' , ), 2016, (2016, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Behaviors' , 'Behaviors' , ), 2017, (2017, (), [ (16393, 10, None, "IID('{914934E3-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'EffectInformation' , 'EffectInformation' , ), 2018, (2018, (), [ (16393, 10, None, "IID('{914934E2-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

EffectInformation_vtables_dispatch_ = 1
EffectInformation_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'AfterEffect' , 'AfterEffect' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'AnimateBackground' , 'AnimateBackground' , ), 2004, (2004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'AnimateTextInReverse' , 'AnimateTextInReverse' , ), 2005, (2005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'BuildByLevelEffect' , 'BuildByLevelEffect' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Dim' , 'Dim' , ), 2007, (2007, (), [ (16393, 10, None, "IID('{91493452-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'PlaySettings' , 'PlaySettings' , ), 2008, (2008, (), [ (16393, 10, None, "IID('{9149348E-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SoundEffect' , 'SoundEffect' , ), 2009, (2009, (), [ (16393, 10, None, "IID('{91493472-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'TextUnitEffect' , 'TextUnitEffect' , ), 2010, (2010, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

EffectParameters_vtables_dispatch_ = 1
EffectParameters_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Direction' , 'Direction' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Direction' , 'Direction' , ), 2003, (2003, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Amount' , 'Amount' , ), 2004, (2004, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Amount' , 'Amount' , ), 2004, (2004, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'Size' , ), 2005, (2005, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'Size' , ), 2005, (2005, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Color2' , 'Color2' , ), 2006, (2006, (), [ (16393, 10, None, "IID('{91493452-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'Relative' , 'Relative' , ), 2007, (2007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Relative' , 'Relative' , ), 2007, (2007, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'FontName' , 'FontName' , ), 2008, (2008, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FontName' , 'FontName' , ), 2008, (2008, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
]

ExtraColors_vtables_dispatch_ = 1
ExtraColors_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Type' , ), 2003, (2003, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

FillFormat_vtables_dispatch_ = 1
FillFormat_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Background' , ), 10, (10, (), [ ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'OneColorGradient' , 'Style' , 'Variant' , 'Degree' , ), 11, (11, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Patterned' , 'Pattern' , ), 12, (12, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'PresetGradient' , 'Style' , 'Variant' , 'PresetGradientType' , ), 13, (13, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'PresetTextured' , 'PresetTexture' , ), 14, (14, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Solid' , ), 15, (15, (), [ ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'TwoColorGradient' , 'Style' , 'Variant' , ), 16, (16, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UserPicture' , 'PictureFile' , ), 17, (17, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'UserTextured' , 'TextureFile' , ), 18, (18, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'BackColor' , 'BackColor' , ), 100, (100, (), [ (16393, 10, None, "IID('{91493452-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'BackColor' , 'BackColor' , ), 100, (100, (), [ (9, 1, None, "IID('{91493452-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ForeColor' , 'ForeColor' , ), 101, (101, (), [ (16393, 10, None, "IID('{91493452-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'ForeColor' , 'ForeColor' , ), 101, (101, (), [ (9, 1, None, "IID('{91493452-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'GradientColorType' , 'GradientColorType' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'GradientDegree' , 'GradientDegree' , ), 103, (103, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GradientStyle' , 'GradientStyle' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'GradientVariant' , 'GradientVariant' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Pattern' , 'Pattern' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'PresetGradientType' , 'PresetGradientType' , ), 107, (107, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'PresetTexture' , 'PresetTexture' , ), 108, (108, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'TextureName' , 'TextureName' , ), 109, (109, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'TextureType' , 'TextureType' , ), 110, (110, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'Transparency' , 'Transparency' , ), 111, (111, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Transparency' , 'Transparency' , ), 111, (111, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 112, (112, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'Visible' , ), 113, (113, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'Visible' , ), 113, (113, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

FilterEffect_vtables_dispatch_ = 1
FilterEffect_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 2003, (2003, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Subtype' , 'Subtype' , ), 2004, (2004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Subtype' , 'Subtype' , ), 2004, (2004, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Reveal' , 'Reveal' , ), 2005, (2005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Reveal' , 'Reveal' , ), 2005, (2005, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

Font_vtables_dispatch_ = 1
Font_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'Color' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{91493452-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Bold' , 'Bold' , ), 2004, (2004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Bold' , 'Bold' , ), 2004, (2004, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Italic' , 'Italic' , ), 2005, (2005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Italic' , 'Italic' , ), 2005, (2005, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Shadow' , 'Shadow' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Shadow' , 'Shadow' , ), 2006, (2006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'Emboss' , 'Emboss' , ), 2007, (2007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Emboss' , 'Emboss' , ), 2007, (2007, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'Underline' , 'Underline' , ), 2008, (2008, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Underline' , 'Underline' , ), 2008, (2008, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'Subscript' , 'Subscript' , ), 2009, (2009, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Subscript' , 'Subscript' , ), 2009, (2009, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'Superscript' , 'Superscript' , ), 2010, (2010, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Superscript' , 'Superscript' , ), 2010, (2010, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'BaselineOffset' , 'BaselineOffset' , ), 2011, (2011, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'BaselineOffset' , 'BaselineOffset' , ), 2011, (2011, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'Embedded' , 'Embedded' , ), 2012, (2012, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Embeddable' , 'Embeddable' , ), 2013, (2013, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'Size' , ), 2014, (2014, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'Size' , ), 2014, (2014, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 2015, (2015, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 2015, (2015, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'NameFarEast' , 'NameFarEast' , ), 2016, (2016, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'NameFarEast' , 'NameFarEast' , ), 2016, (2016, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'NameAscii' , 'NameAscii' , ), 2017, (2017, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'NameAscii' , 'NameAscii' , ), 2017, (2017, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'AutoRotateNumbers' , 'AutoRotateNumbers' , ), 2018, (2018, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'AutoRotateNumbers' , 'AutoRotateNumbers' , ), 2018, (2018, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( 'NameOther' , 'NameOther' , ), 2019, (2019, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'NameOther' , 'NameOther' , ), 2019, (2019, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( 'NameComplexScript' , 'NameComplexScript' , ), 2020, (2020, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'NameComplexScript' , 'NameComplexScript' , ), 2020, (2020, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
]

Fonts_vtables_dispatch_ = 1
Fonts_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			(16393, 10, None, "IID('{91493495-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Replace' , 'Original' , 'Replacement' , ), 2003, (2003, (), [ (8, 1, None, None) , 
			(8, 1, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

FreeformBuilder_vtables_dispatch_ = 1
FreeformBuilder_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'AddNodes' , 'SegmentType' , 'EditingType' , 'X1' , 'Y1' , 
			'X2' , 'Y2' , 'X3' , 'Y3' , ), 10, (10, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (4, 49, '0.0', None) , 
			(4, 49, '0.0', None) , (4, 49, '0.0', None) , (4, 49, '0.0', None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'ConvertToShape' , 'Freeform' , ), 11, (11, (), [ (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
]

GroupShapes_vtables_dispatch_ = 1
GroupShapes_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'ppidisp' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pnShapes' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			(16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppienum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 1024 , )),
	(( 'Range' , 'Index' , 'Range' , ), 10, (10, (), [ (12, 1, None, None) , 
			(16393, 10, None, "IID('{9149347A-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

HeaderFooter_vtables_dispatch_ = 1
HeaderFooter_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'Visible' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'Visible' , ), 2003, (2003, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'Text' , ), 2004, (2004, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'Text' , ), 2004, (2004, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'UseFormat' , 'UseFormat' , ), 2005, (2005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'UseFormat' , 'UseFormat' , ), 2005, (2005, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Format' , 'Format' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'Format' , 'Format' , ), 2006, (2006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

HeadersFooters_vtables_dispatch_ = 1
HeadersFooters_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'DateAndTime' , 'DateAndTime' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{9149349C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'SlideNumber' , 'SlideNumber' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{9149349C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Header' , 'Header' , ), 2005, (2005, (), [ (16393, 10, None, "IID('{9149349C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Footer' , 'Footer' , ), 2006, (2006, (), [ (16393, 10, None, "IID('{9149349C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'DisplayOnTitleSlide' , 'DisplayOnTitleSlide' , ), 2007, (2007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'DisplayOnTitleSlide' , 'DisplayOnTitleSlide' , ), 2007, (2007, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Clear' , ), 2008, (2008, (), [ ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
]

Hyperlink_vtables_dispatch_ = 1
Hyperlink_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Address' , 'Address' , ), 2004, (2004, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Address' , 'Address' , ), 2004, (2004, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'SubAddress' , 'SubAddress' , ), 2005, (2005, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'SubAddress' , 'SubAddress' , ), 2005, (2005, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'AddToFavorites' , ), 2006, (2006, (), [ ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'EmailSubject' , 'EmailSubject' , ), 2007, (2007, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'EmailSubject' , 'EmailSubject' , ), 2007, (2007, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ScreenTip' , 'ScreenTip' , ), 2008, (2008, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'ScreenTip' , 'ScreenTip' , ), 2008, (2008, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'TextToDisplay' , 'TextToDisplay' , ), 2009, (2009, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'TextToDisplay' , 'TextToDisplay' , ), 2009, (2009, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ShowAndReturn' , 'ShowAndReturn' , ), 2010, (2010, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'ShowAndReturn' , 'ShowAndReturn' , ), 2010, (2010, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Follow' , ), 2011, (2011, (), [ ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'CreateNewDocument' , 'FileName' , 'EditNow' , 'Overwrite' , ), 2012, (2012, (), [ 
			(8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 2013, (2013, (), [ ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
]

Hyperlinks_vtables_dispatch_ = 1
Hyperlinks_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{91493465-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

LineFormat_vtables_dispatch_ = 1
LineFormat_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'BackColor' , 'BackColor' , ), 100, (100, (), [ (16393, 10, None, "IID('{91493452-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'BackColor' , 'BackColor' , ), 100, (100, (), [ (9, 1, None, "IID('{91493452-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'BeginArrowheadLength' , 'BeginArrowheadLength' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'BeginArrowheadLength' , 'BeginArrowheadLength' , ), 101, (101, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'BeginArrowheadStyle' , 'BeginArrowheadStyle' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'BeginArrowheadStyle' , 'BeginArrowheadStyle' , ), 102, (102, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'BeginArrowheadWidth' , 'BeginArrowheadWidth' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'BeginArrowheadWidth' , 'BeginArrowheadWidth' , ), 103, (103, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'DashStyle' , 'DashStyle' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'DashStyle' , 'DashStyle' , ), 104, (104, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'EndArrowheadLength' , 'EndArrowheadLength' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'EndArrowheadLength' , 'EndArrowheadLength' , ), 105, (105, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'EndArrowheadStyle' , 'EndArrowheadStyle' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'EndArrowheadStyle' , 'EndArrowheadStyle' , ), 106, (106, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'EndArrowheadWidth' , 'EndArrowheadWidth' , ), 107, (107, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'EndArrowheadWidth' , 'EndArrowheadWidth' , ), 107, (107, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'ForeColor' , 'ForeColor' , ), 108, (108, (), [ (16393, 10, None, "IID('{91493452-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ForeColor' , 'ForeColor' , ), 108, (108, (), [ (9, 1, None, "IID('{91493452-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 4 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'Pattern' , 'Pattern' , ), 109, (109, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Pattern' , 'Pattern' , ), 109, (109, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'Style' , 'Style' , ), 110, (110, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Style' , 'Style' , ), 110, (110, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'Transparency' , 'Transparency' , ), 111, (111, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Transparency' , 'Transparency' , ), 111, (111, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'Visible' , ), 112, (112, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'Visible' , ), 112, (112, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'Weight' , 'Weight' , ), 113, (113, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Weight' , 'Weight' , ), 113, (113, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( 'InsetPen' , 'InsetPen' , ), 114, (114, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'InsetPen' , 'InsetPen' , ), 114, (114, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
]

LinkFormat_vtables_dispatch_ = 1
LinkFormat_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'SourceFullName' , 'SourceFullName' , ), 2003, (2003, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'SourceFullName' , 'SourceFullName' , ), 2003, (2003, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'AutoUpdate' , 'AutoUpdate' , ), 2004, (2004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'AutoUpdate' , 'AutoUpdate' , ), 2004, (2004, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Update' , ), 2005, (2005, (), [ ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

MasterEvents_vtables_dispatch_ = 0
MasterEvents_vtables_ = [
]

MotionEffect_vtables_dispatch_ = 1
MotionEffect_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'ByX' , 'ByX' , ), 2003, (2003, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'ByX' , 'ByX' , ), 2003, (2003, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'ByY' , 'ByY' , ), 2004, (2004, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'ByY' , 'ByY' , ), 2004, (2004, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'FromX' , 'FromX' , ), 2005, (2005, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'FromX' , 'FromX' , ), 2005, (2005, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FromY' , 'FromY' , ), 2006, (2006, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'FromY' , 'FromY' , ), 2006, (2006, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ToX' , 'ToX' , ), 2007, (2007, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'ToX' , 'ToX' , ), 2007, (2007, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ToY' , 'ToY' , ), 2008, (2008, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'ToY' , 'ToY' , ), 2008, (2008, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Path' , 'Path' , ), 2009, (2009, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'Path' , 'Path' , ), 2009, (2009, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

MouseDownHandler_vtables_dispatch_ = 0
MouseDownHandler_vtables_ = [
	(( 'OnMouseDown' , 'activeWin' , ), 2001, (2001, (), [ (13, 1, None, None) , ], 1 , 1 , 4 , 0 , 12 , (3, 0, None, None) , 0 , )),
]

MouseTracker_vtables_dispatch_ = 0
MouseTracker_vtables_ = [
	(( 'OnTrack' , 'X' , 'Y' , ), 2001, (2001, (), [ (4, 1, None, None) , 
			(4, 1, None, None) , ], 1 , 1 , 4 , 0 , 12 , (3, 0, None, None) , 0 , )),
	(( 'EndTrack' , 'X' , 'Y' , ), 2002, (2002, (), [ (4, 1, None, None) , 
			(4, 1, None, None) , ], 1 , 1 , 4 , 0 , 16 , (3, 0, None, None) , 0 , )),
]

NamedSlideShow_vtables_dispatch_ = 1
NamedSlideShow_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 2003, (2003, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 2004, (2004, (), [ ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'SlideIDs' , 'SlideIDs' , ), 2005, (2005, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

NamedSlideShows_vtables_dispatch_ = 1
NamedSlideShows_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			(16393, 10, None, "IID('{9149345C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Name' , 'safeArrayOfSlideIDs' , 'Add' , ), 2003, (2003, (), [ 
			(8, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{9149345C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

OCXExtender_vtables_dispatch_ = 1
OCXExtender_vtables_ = [
	(( 'Visible' , 'Visible' , ), -2147418105, (-2147418105, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'Visible' , ), -2147418105, (-2147418105, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Left' , 'Left' , ), -2147418109, (-2147418109, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Left' , 'Left' , ), -2147418109, (-2147418109, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Top' , 'Top' , ), -2147418108, (-2147418108, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Top' , 'Top' , ), -2147418108, (-2147418108, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'Height' , ), -2147418107, (-2147418107, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'Height' , ), -2147418107, (-2147418107, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), -2147418106, (-2147418106, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), -2147418106, (-2147418106, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ZOrderPosition' , 'ZOrderPosition' , ), -2147417882, (-2147417882, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), -2147418112, (-2147418112, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), -2147418112, (-2147418112, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'AltHTML' , 'AltHTML' , ), -2147417881, (-2147417881, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 64 , )),
	(( 'AltHTML' , 'AltHTML' , ), -2147417881, (-2147417881, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 84 , (3, 0, None, None) , 64 , )),
]

OLEFormat_vtables_dispatch_ = 1
OLEFormat_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'ObjectVerbs' , 'ObjectVerbs' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{9149348A-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Object' , 'Object' , ), 2004, (2004, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'ProgID' , 'ProgID' , ), 2005, (2005, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'FollowColors' , 'FollowColors' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'FollowColors' , 'FollowColors' , ), 2006, (2006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'DoVerb' , 'Index' , ), 2007, (2007, (), [ (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Activate' , ), 2008, (2008, (), [ ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
]

ObjectVerbs_vtables_dispatch_ = 1
ObjectVerbs_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

Options_vtables_dispatch_ = 1
Options_vtables_ = [
	(( 'DisplayPasteOptions' , 'DisplayPasteOptions' , ), 2001, (2001, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'DisplayPasteOptions' , 'DisplayPasteOptions' , ), 2001, (2001, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
]

PageSetup_vtables_dispatch_ = 1
PageSetup_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'FirstSlideNumber' , 'FirstSlideNumber' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'FirstSlideNumber' , 'FirstSlideNumber' , ), 2003, (2003, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'SlideHeight' , 'SlideHeight' , ), 2004, (2004, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'SlideHeight' , 'SlideHeight' , ), 2004, (2004, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'SlideWidth' , 'SlideWidth' , ), 2005, (2005, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'SlideWidth' , 'SlideWidth' , ), 2005, (2005, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SlideSize' , 'SlideSize' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'SlideSize' , 'SlideSize' , ), 2006, (2006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'NotesOrientation' , 'NotesOrientation' , ), 2007, (2007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'NotesOrientation' , 'NotesOrientation' , ), 2007, (2007, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SlideOrientation' , 'SlideOrientation' , ), 2008, (2008, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'SlideOrientation' , 'SlideOrientation' , ), 2008, (2008, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

Pane_vtables_dispatch_ = 1
Pane_vtables_ = [
	(( 'Parent' , 'Parent' , ), 2000, (2000, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Activate' , ), 2001, (2001, (), [ ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Active' , 'Active' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'Application' , ), 2003, (2003, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'ViewType' , 'ViewType' , ), 2004, (2004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
]

Panes_vtables_dispatch_ = 1
Panes_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{914934CC-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

ParagraphFormat_vtables_dispatch_ = 1
ParagraphFormat_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Alignment' , 'Alignment' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Alignment' , 'Alignment' , ), 2003, (2003, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Bullet' , 'Bullet' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{91493497-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'LineRuleBefore' , 'LineRuleBefore' , ), 2005, (2005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'LineRuleBefore' , 'LineRuleBefore' , ), 2005, (2005, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'LineRuleAfter' , 'LineRuleAfter' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LineRuleAfter' , 'LineRuleAfter' , ), 2006, (2006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'LineRuleWithin' , 'LineRuleWithin' , ), 2007, (2007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'LineRuleWithin' , 'LineRuleWithin' , ), 2007, (2007, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'SpaceBefore' , 'SpaceBefore' , ), 2008, (2008, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SpaceBefore' , 'SpaceBefore' , ), 2008, (2008, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'SpaceAfter' , 'SpaceAfter' , ), 2009, (2009, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SpaceAfter' , 'SpaceAfter' , ), 2009, (2009, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'SpaceWithin' , 'SpaceWithin' , ), 2010, (2010, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SpaceWithin' , 'SpaceWithin' , ), 2010, (2010, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'BaseLineAlignment' , 'BaseLineAlignment' , ), 2011, (2011, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'BaseLineAlignment' , 'BaseLineAlignment' , ), 2011, (2011, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'FarEastLineBreakControl' , 'FarEastLineBreakControl' , ), 2012, (2012, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'FarEastLineBreakControl' , 'FarEastLineBreakControl' , ), 2012, (2012, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'WordWrap' , 'WordWrap' , ), 2013, (2013, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'WordWrap' , 'WordWrap' , ), 2013, (2013, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'HangingPunctuation' , 'HangingPunctuation' , ), 2014, (2014, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'HangingPunctuation' , 'HangingPunctuation' , ), 2014, (2014, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'TextDirection' , 'TextDirection' , ), 2015, (2015, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'TextDirection' , 'TextDirection' , ), 2015, (2015, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
]

PictureFormat_vtables_dispatch_ = 1
PictureFormat_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'IncrementBrightness' , 'Increment' , ), 10, (10, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'IncrementContrast' , 'Increment' , ), 11, (11, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Brightness' , 'Brightness' , ), 100, (100, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Brightness' , 'Brightness' , ), 100, (100, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'ColorType' , 'ColorType' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ColorType' , 'ColorType' , ), 101, (101, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'Contrast' , 'Contrast' , ), 102, (102, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Contrast' , 'Contrast' , ), 102, (102, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'CropBottom' , 'CropBottom' , ), 103, (103, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'CropBottom' , 'CropBottom' , ), 103, (103, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'CropLeft' , 'CropLeft' , ), 104, (104, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'CropLeft' , 'CropLeft' , ), 104, (104, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'CropRight' , 'CropRight' , ), 105, (105, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'CropRight' , 'CropRight' , ), 105, (105, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'CropTop' , 'CropTop' , ), 106, (106, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'CropTop' , 'CropTop' , ), 106, (106, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'TransparencyColor' , 'TransparencyColor' , ), 107, (107, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'TransparencyColor' , 'TransparencyColor' , ), 107, (107, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'TransparentBackground' , 'TransparentBackground' , ), 108, (108, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'TransparentBackground' , 'TransparentBackground' , ), 108, (108, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
]

PlaceholderFormat_vtables_dispatch_ = 1
PlaceholderFormat_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
]

Placeholders_vtables_dispatch_ = 1
Placeholders_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

PlaySettings_vtables_dispatch_ = 1
PlaySettings_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'ActionVerb' , 'ActionVerb' , ), 2003, (2003, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'ActionVerb' , 'ActionVerb' , ), 2003, (2003, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'HideWhileNotPlaying' , 'HideWhileNotPlaying' , ), 2004, (2004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'HideWhileNotPlaying' , 'HideWhileNotPlaying' , ), 2004, (2004, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'LoopUntilStopped' , 'LoopUntilStopped' , ), 2005, (2005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'LoopUntilStopped' , 'LoopUntilStopped' , ), 2005, (2005, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'PlayOnEntry' , 'PlayOnEntry' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'PlayOnEntry' , 'PlayOnEntry' , ), 2006, (2006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'RewindMovie' , 'RewindMovie' , ), 2007, (2007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'RewindMovie' , 'RewindMovie' , ), 2007, (2007, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'PauseAnimation' , 'PauseAnimation' , ), 2008, (2008, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'PauseAnimation' , 'PauseAnimation' , ), 2008, (2008, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'StopAfterSlides' , 'StopAfterSlides' , ), 2009, (2009, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'StopAfterSlides' , 'StopAfterSlides' , ), 2009, (2009, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

PresEvents_vtables_dispatch_ = 0
PresEvents_vtables_ = [
]

Presentations_vtables_dispatch_ = 1
Presentations_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			(16397, 10, None, "IID('{91493444-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'WithWindow' , 'Add' , ), 2003, (2003, (), [ (3, 49, '-1', None) , 
			(16397, 10, None, "IID('{91493444-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'OpenOld' , 'FileName' , 'ReadOnly' , 'Untitled' , 'WithWindow' , 
			'OpenOld' , ), 2004, (2004, (), [ (8, 1, None, None) , (3, 49, '0', None) , (3, 49, '0', None) , 
			(3, 49, '-1', None) , (16397, 10, None, "IID('{91493444-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 64 , )),
	(( 'Open' , 'FileName' , 'ReadOnly' , 'Untitled' , 'WithWindow' , 
			'Open' , ), 2005, (2005, (), [ (8, 1, None, None) , (3, 49, '0', None) , (3, 49, '0', None) , 
			(3, 49, '-1', None) , (16397, 10, None, "IID('{91493444-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'CheckOut' , 'FileName' , ), 2006, (2006, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'CanCheckOut' , 'FileName' , 'CanCheckOut' , ), 2007, (2007, (), [ (8, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
]

PrintOptions_vtables_dispatch_ = 1
PrintOptions_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'PrintColorType' , 'PrintColorType' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'PrintColorType' , 'PrintColorType' , ), 2002, (2002, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Collate' , 'Collate' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Collate' , 'Collate' , ), 2003, (2003, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'FitToPage' , 'FitToPage' , ), 2004, (2004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'FitToPage' , 'FitToPage' , ), 2004, (2004, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'FrameSlides' , 'FrameSlides' , ), 2005, (2005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FrameSlides' , 'FrameSlides' , ), 2005, (2005, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfCopies' , 'NumberOfCopies' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfCopies' , 'NumberOfCopies' , ), 2006, (2006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'OutputType' , 'OutputType' , ), 2007, (2007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'OutputType' , 'OutputType' , ), 2007, (2007, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2008, (2008, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'PrintHiddenSlides' , 'PrintHiddenSlides' , ), 2009, (2009, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'PrintHiddenSlides' , 'PrintHiddenSlides' , ), 2009, (2009, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'PrintInBackground' , 'PrintInBackground' , ), 2010, (2010, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'PrintInBackground' , 'PrintInBackground' , ), 2010, (2010, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'RangeType' , 'RangeType' , ), 2011, (2011, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'RangeType' , 'RangeType' , ), 2011, (2011, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Ranges' , 'Ranges' , ), 2012, (2012, (), [ (16393, 10, None, "IID('{9149345E-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'PrintFontsAsGraphics' , 'PrintFontsAsGraphics' , ), 2013, (2013, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'PrintFontsAsGraphics' , 'PrintFontsAsGraphics' , ), 2013, (2013, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'SlideShowName' , 'SlideShowName' , ), 2014, (2014, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SlideShowName' , 'SlideShowName' , ), 2014, (2014, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'ActivePrinter' , 'ActivePrinter' , ), 2015, (2015, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ActivePrinter' , 'ActivePrinter' , ), 2015, (2015, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'HandoutOrder' , 'HandoutOrder' , ), 2016, (2016, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'HandoutOrder' , 'HandoutOrder' , ), 2016, (2016, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'PrintComments' , 'PrintComments' , ), 2017, (2017, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PrintComments' , 'PrintComments' , ), 2017, (2017, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
]

PrintRange_vtables_dispatch_ = 1
PrintRange_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Start' , 'Start' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'End' , 'End' , ), 2004, (2004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 2005, (2005, (), [ ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
]

PrintRanges_vtables_dispatch_ = 1
PrintRanges_vtables_ = [
	(( 'Add' , 'Start' , 'End' , 'Add' , ), 2001, (2001, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{9149345F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'Application' , ), 2002, (2002, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'ClearAll' , ), 2003, (2003, (), [ ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{9149345F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2004, (2004, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

PropertyEffect_vtables_dispatch_ = 1
PropertyEffect_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Property' , 'Property' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Property' , 'Property' , ), 2003, (2003, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Points' , 'Points' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{914934EA-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'From' , 'From' , ), 2005, (2005, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'From' , 'From' , ), 2005, (2005, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'To' , 'To' , ), 2006, (2006, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'To' , 'To' , ), 2006, (2006, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
]

PublishObject_vtables_dispatch_ = 1
PublishObject_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'HTMLVersion' , 'HTMLVersion' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'HTMLVersion' , 'HTMLVersion' , ), 2003, (2003, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'SourceType' , 'SourceType' , ), 2004, (2004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'SourceType' , 'SourceType' , ), 2004, (2004, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'RangeStart' , 'RangeStart' , ), 2005, (2005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'RangeStart' , 'RangeStart' , ), 2005, (2005, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'RangeEnd' , 'RangeEnd' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'RangeEnd' , 'RangeEnd' , ), 2006, (2006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SlideShowName' , 'SlideShowName' , ), 2007, (2007, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'SlideShowName' , 'SlideShowName' , ), 2007, (2007, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SpeakerNotes' , 'SpeakerNotes' , ), 2008, (2008, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'SpeakerNotes' , 'SpeakerNotes' , ), 2008, (2008, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'FileName' , ), 2009, (2009, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'FileName' , ), 2009, (2009, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Publish' , ), 2010, (2010, (), [ ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
]

PublishObjects_vtables_dispatch_ = 1
PublishObjects_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{914934D0-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

RGBColor_vtables_dispatch_ = 1
RGBColor_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'RGB' , 'RGB' , ), 0, (0, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'RGB' , 'RGB' , ), 0, (0, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
]

RotationEffect_vtables_dispatch_ = 1
RotationEffect_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'By' , 'By' , ), 2003, (2003, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'By' , 'By' , ), 2003, (2003, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'From' , 'From' , ), 2004, (2004, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'From' , 'From' , ), 2004, (2004, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'To' , 'To' , ), 2005, (2005, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'To' , 'To' , ), 2005, (2005, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

Row_vtables_dispatch_ = 1
Row_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Cells' , 'Cells' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{914934C8-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Select' , ), 2004, (2004, (), [ ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 2005, (2005, (), [ ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'Height' , ), 2006, (2006, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'Height' , ), 2006, (2006, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

Rows_vtables_dispatch_ = 1
Rows_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{914934C7-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'BeforeRow' , 'Add' , ), 2003, (2003, (), [ (3, 49, '-1', None) , 
			(16393, 10, None, "IID('{914934C7-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

Ruler_vtables_dispatch_ = 1
Ruler_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'TabStops' , 'TabStops' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{91493493-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Levels' , 'Levels' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{91493491-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
]

RulerLevel_vtables_dispatch_ = 1
RulerLevel_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'FirstMargin' , 'FirstMargin' , ), 2003, (2003, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'FirstMargin' , 'FirstMargin' , ), 2003, (2003, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'LeftMargin' , 'LeftMargin' , ), 2004, (2004, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'LeftMargin' , 'LeftMargin' , ), 2004, (2004, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

RulerLevels_vtables_dispatch_ = 1
RulerLevels_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{91493492-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

ScaleEffect_vtables_dispatch_ = 1
ScaleEffect_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'ByX' , 'ByX' , ), 2003, (2003, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'ByX' , 'ByX' , ), 2003, (2003, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'ByY' , 'ByY' , ), 2004, (2004, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'ByY' , 'ByY' , ), 2004, (2004, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'FromX' , 'FromX' , ), 2005, (2005, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'FromX' , 'FromX' , ), 2005, (2005, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FromY' , 'FromY' , ), 2006, (2006, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'FromY' , 'FromY' , ), 2006, (2006, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ToX' , 'ToX' , ), 2007, (2007, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'ToX' , 'ToX' , ), 2007, (2007, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ToY' , 'ToY' , ), 2008, (2008, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'ToY' , 'ToY' , ), 2008, (2008, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

Selection_vtables_dispatch_ = 1
Selection_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Cut' , ), 2003, (2003, (), [ ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Copy' , ), 2004, (2004, (), [ ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 2005, (2005, (), [ ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Unselect' , ), 2006, (2006, (), [ ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 2007, (2007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'SlideRange' , 'SlideRange' , ), 2008, (2008, (), [ (16393, 10, None, "IID('{9149346B-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ShapeRange' , 'ShapeRange' , ), 2009, (2009, (), [ (16393, 10, None, "IID('{9149347A-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'TextRange' , 'TextRange' , ), 2010, (2010, (), [ (16393, 10, None, "IID('{9149348F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ChildShapeRange' , 'ChildShapeRange' , ), 2011, (2011, (), [ (16393, 10, None, "IID('{9149347A-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'HasChildShapeRange' , 'HasChildShapeRange' , ), 2012, (2012, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

Sequence_vtables_dispatch_ = 1
Sequence_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{914934DF-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'AddEffect' , 'Shape' , 'effectId' , 'Level' , 'trigger' , 
			'Index' , 'Effect' , ), 2003, (2003, (), [ (9, 1, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , (3, 1, None, None) , 
			(3, 49, '0', None) , (3, 49, '1', None) , (3, 49, '-1', None) , (16393, 10, None, "IID('{914934DF-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Clone' , 'Effect' , 'Index' , 'Clone' , ), 2004, (2004, (), [ 
			(9, 1, None, "IID('{914934DF-5A91-11CF-8700-00AA0060263B}')") , (3, 49, '-1', None) , (16393, 10, None, "IID('{914934DF-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FindFirstAnimationFor' , 'Shape' , 'FindFirstAnimationFor' , ), 2005, (2005, (), [ (9, 1, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , 
			(16393, 10, None, "IID('{914934DF-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'FindFirstAnimationForClick' , 'click' , 'FindFirstAnimationForClick' , ), 2006, (2006, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{914934DF-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ConvertToBuildLevel' , 'Effect' , 'Level' , 'ConvertToBuildLevel' , ), 2007, (2007, (), [ 
			(9, 1, None, "IID('{914934DF-5A91-11CF-8700-00AA0060263B}')") , (3, 1, None, None) , (16393, 10, None, "IID('{914934DF-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'ConvertToAfterEffect' , 'Effect' , 'After' , 'DimColor' , 'DimSchemeColor' , 
			'ConvertToAfterEffect' , ), 2008, (2008, (), [ (9, 1, None, "IID('{914934DF-5A91-11CF-8700-00AA0060263B}')") , (3, 1, None, None) , (3, 49, '0', None) , 
			(3, 49, '0', None) , (16393, 10, None, "IID('{914934DF-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ConvertToAnimateBackground' , 'Effect' , 'AnimateBackground' , 'ConvertToAnimateBackground' , ), 2009, (2009, (), [ 
			(9, 1, None, "IID('{914934DF-5A91-11CF-8700-00AA0060263B}')") , (3, 1, None, None) , (16393, 10, None, "IID('{914934DF-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'ConvertToAnimateInReverse' , 'Effect' , 'animateInReverse' , 'ConvertToAnimateInReverse' , ), 2010, (2010, (), [ 
			(9, 1, None, "IID('{914934DF-5A91-11CF-8700-00AA0060263B}')") , (3, 1, None, None) , (16393, 10, None, "IID('{914934DF-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ConvertToTextUnitEffect' , 'Effect' , 'unitEffect' , 'ConvertToTextUnitEffect' , ), 2011, (2011, (), [ 
			(9, 1, None, "IID('{914934DF-5A91-11CF-8700-00AA0060263B}')") , (3, 1, None, None) , (16393, 10, None, "IID('{914934DF-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
]

Sequences_vtables_dispatch_ = 1
Sequences_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{914934DE-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Index' , 'Add' , ), 2003, (2003, (), [ (3, 49, '-1', None) , 
			(16393, 10, None, "IID('{914934DE-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

SetEffect_vtables_dispatch_ = 1
SetEffect_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Property' , 'Property' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Property' , 'Property' , ), 2003, (2003, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'To' , 'To' , ), 2004, (2004, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'To' , 'To' , ), 2004, (2004, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

ShadowFormat_vtables_dispatch_ = 1
ShadowFormat_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'IncrementOffsetX' , 'Increment' , ), 10, (10, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'IncrementOffsetY' , 'Increment' , ), 11, (11, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'ForeColor' , 'ForeColor' , ), 100, (100, (), [ (16393, 10, None, "IID('{91493452-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'ForeColor' , 'ForeColor' , ), 100, (100, (), [ (9, 1, None, "IID('{91493452-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Obscured' , 'Obscured' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Obscured' , 'Obscured' , ), 101, (101, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'OffsetX' , 'OffsetX' , ), 102, (102, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'OffsetX' , 'OffsetX' , ), 102, (102, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'OffsetY' , 'OffsetY' , ), 103, (103, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'OffsetY' , 'OffsetY' , ), 103, (103, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'Transparency' , 'Transparency' , ), 104, (104, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Transparency' , 'Transparency' , ), 104, (104, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 105, (105, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'Visible' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'Visible' , ), 106, (106, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
]

Shape_vtables_dispatch_ = 1
Shape_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Apply' , ), 10, (10, (), [ ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 11, (11, (), [ ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Flip' , 'FlipCmd' , ), 13, (13, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'IncrementLeft' , 'Increment' , ), 14, (14, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'IncrementRotation' , 'Increment' , ), 15, (15, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'IncrementTop' , 'Increment' , ), 16, (16, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'PickUp' , ), 17, (17, (), [ ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'RerouteConnections' , ), 18, (18, (), [ ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'ScaleHeight' , 'Factor' , 'RelativeToOriginalSize' , 'fScale' , ), 19, (19, (), [ 
			(4, 1, None, None) , (3, 1, None, None) , (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ScaleWidth' , 'Factor' , 'RelativeToOriginalSize' , 'fScale' , ), 20, (20, (), [ 
			(4, 1, None, None) , (3, 1, None, None) , (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'SetShapesDefaultProperties' , ), 22, (22, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Ungroup' , 'Ungroup' , ), 23, (23, (), [ (16393, 10, None, "IID('{9149347A-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'ZOrder' , 'ZOrderCmd' , ), 24, (24, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Adjustments' , 'Adjustments' , ), 100, (100, (), [ (16393, 10, None, "IID('{9149347C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'AutoShapeType' , 'AutoShapeType' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'AutoShapeType' , 'AutoShapeType' , ), 101, (101, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'BlackWhiteMode' , 'BlackWhiteMode' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'BlackWhiteMode' , 'BlackWhiteMode' , ), 102, (102, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'Callout' , 'Callout' , ), 103, (103, (), [ (16393, 10, None, "IID('{91493485-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionSiteCount' , 'ConnectionSiteCount' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'Connector' , 'Connector' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ConnectorFormat' , 'ConnectorFormat' , ), 106, (106, (), [ (16393, 10, None, "IID('{91493481-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'Fill' , 'Fill' , ), 107, (107, (), [ (16393, 10, None, "IID('{9149347E-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'GroupItems' , 'GroupItems' , ), 108, (108, (), [ (16393, 10, None, "IID('{9149347B-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'Height' , ), 109, (109, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'Height' , ), 109, (109, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'HorizontalFlip' , 'HorizontalFlip' , ), 110, (110, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Left' , 'Left' , ), 111, (111, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( 'Left' , 'Left' , ), 111, (111, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Line' , 'Line' , ), 112, (112, (), [ (16393, 10, None, "IID('{9149347F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( 'LockAspectRatio' , 'LockAspectRatio' , ), 113, (113, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'LockAspectRatio' , 'LockAspectRatio' , ), 113, (113, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 115, (115, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 115, (115, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( 'Nodes' , 'Nodes' , ), 116, (116, (), [ (16393, 10, None, "IID('{91493486-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Rotation' , 'Rotation' , ), 117, (117, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( 'Rotation' , 'Rotation' , ), 117, (117, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'PictureFormat' , 'Picture' , ), 118, (118, (), [ (16393, 10, None, "IID('{9149347D-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
	(( 'Shadow' , 'Shadow' , ), 119, (119, (), [ (16393, 10, None, "IID('{91493480-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'TextEffect' , 'TextEffect' , ), 120, (120, (), [ (16393, 10, None, "IID('{91493482-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 196 , (3, 0, None, None) , 0 , )),
	(( 'TextFrame' , 'TextFrame' , ), 121, (121, (), [ (16393, 10, None, "IID('{91493484-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ThreeD' , 'ThreeD' , ), 122, (122, (), [ (16393, 10, None, "IID('{91493483-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 204 , (3, 0, None, None) , 0 , )),
	(( 'Top' , 'Top' , ), 123, (123, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Top' , 'Top' , ), 123, (123, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 212 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 124, (124, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'VerticalFlip' , 'VerticalFlip' , ), 125, (125, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 220 , (3, 0, None, None) , 0 , )),
	(( 'Vertices' , 'Vertices' , ), 126, (126, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'Visible' , ), 127, (127, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 228 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'Visible' , ), 127, (127, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 128, (128, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 236 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 128, (128, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ZOrderPosition' , 'ZOrderPosition' , ), 129, (129, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 244 , (3, 0, None, None) , 0 , )),
	(( 'OLEFormat' , 'OLEFormat' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{91493488-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'LinkFormat' , 'LinkFormat' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{91493489-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 252 , (3, 0, None, None) , 0 , )),
	(( 'PlaceholderFormat' , 'PlaceholderFormat' , ), 2005, (2005, (), [ (16393, 10, None, "IID('{91493477-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'AnimationSettings' , 'AnimationSettings' , ), 2006, (2006, (), [ (16393, 10, None, "IID('{9149348B-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 260 , (3, 0, None, None) , 0 , )),
	(( 'ActionSettings' , 'ActionSettings' , ), 2007, (2007, (), [ (16393, 10, None, "IID('{9149348C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Tags' , 'Tags' , ), 2008, (2008, (), [ (16393, 10, None, "IID('{914934B9-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 268 , (3, 0, None, None) , 0 , )),
	(( 'Cut' , ), 2009, (2009, (), [ ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Copy' , ), 2010, (2010, (), [ ], 1 , 1 , 4 , 0 , 276 , (3, 0, None, None) , 0 , )),
	(( 'Select' , 'Replace' , ), 2011, (2011, (), [ (3, 49, '-1', None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Duplicate' , 'Duplicate' , ), 2012, (2012, (), [ (16393, 10, None, "IID('{9149347A-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 284 , (3, 0, None, None) , 0 , )),
	(( 'MediaType' , 'MediaType' , ), 2013, (2013, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'HasTextFrame' , 'HasTextFrame' , ), 2014, (2014, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 292 , (3, 0, None, None) , 0 , )),
	(( 'SoundFormat' , 'SoundFormat' , ), 2015, (2015, (), [ (16393, 10, None, "IID('{91493473-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 64 , )),
	(( 'Script' , 'Script' , ), 130, (130, (), [ (16393, 10, None, "IID('{000C0341-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 300 , (3, 0, None, None) , 0 , )),
	(( 'AlternativeText' , 'AlternativeText' , ), 131, (131, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'AlternativeText' , 'AlternativeText' , ), 131, (131, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 308 , (3, 0, None, None) , 0 , )),
	(( 'HasTable' , 'HasTable' , ), 2016, (2016, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Table' , 'Table' , ), 2017, (2017, (), [ (16393, 10, None, "IID('{914934C3-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 316 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'PathName' , 'Filter' , 'ScaleWidth' , 'ScaleHeight' , 
			'ExportMode' , ), 2018, (2018, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 49, '0', None) , 
			(3, 49, '0', None) , (3, 49, '1', None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 64 , )),
	(( 'HasDiagram' , 'pHasDiagram' , ), 132, (132, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 324 , (3, 0, None, None) , 0 , )),
	(( 'Diagram' , 'Diagram' , ), 133, (133, (), [ (16393, 10, None, "IID('{914934DB-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'HasDiagramNode' , 'pHasDiagram' , ), 134, (134, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 332 , (3, 0, None, None) , 0 , )),
	(( 'DiagramNode' , 'DiagramNode' , ), 135, (135, (), [ (16393, 10, None, "IID('{914934D8-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Child' , 'Child' , ), 136, (136, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 340 , (3, 0, None, None) , 0 , )),
	(( 'ParentGroup' , 'Parent' , ), 137, (137, (), [ (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'CanvasItems' , 'CanvasShapes' , ), 138, (138, (), [ (16393, 10, None, "IID('{914934EC-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 348 , (3, 0, None, None) , 64 , )),
	(( 'Id' , 'pid' , ), 139, (139, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'CanvasCropLeft' , 'Increment' , ), 140, (140, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 356 , (3, 0, None, None) , 64 , )),
	(( 'CanvasCropTop' , 'Increment' , ), 141, (141, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 64 , )),
	(( 'CanvasCropRight' , 'Increment' , ), 142, (142, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 364 , (3, 0, None, None) , 64 , )),
	(( 'CanvasCropBottom' , 'Increment' , ), 143, (143, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 64 , )),
	(( 'RTF' , ), 144, (144, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 372 , (3, 0, None, None) , 64 , )),
]

ShapeNode_vtables_dispatch_ = 1
ShapeNode_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'EditingType' , 'EditingType' , ), 100, (100, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Points' , 'Points' , ), 101, (101, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'SegmentType' , 'SegmentType' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

ShapeNodes_vtables_dispatch_ = 1
ShapeNodes_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			(16393, 10, None, "IID('{91493487-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , '_NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 1024 , )),
	(( 'Delete' , 'Index' , ), 11, (11, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Insert' , 'Index' , 'SegmentType' , 'EditingType' , 'X1' , 
			'Y1' , 'X2' , 'Y2' , 'X3' , 'Y3' , 
			), 12, (12, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (4, 49, '0.0', None) , (4, 49, '0.0', None) , (4, 49, '0.0', None) , (4, 49, '0.0', None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SetEditingType' , 'Index' , 'EditingType' , ), 13, (13, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'SetPosition' , 'Index' , 'X1' , 'Y1' , ), 14, (14, (), [ 
			(3, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SetSegmentType' , 'Index' , 'SegmentType' , ), 15, (15, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
]

ShapeRange_vtables_dispatch_ = 1
ShapeRange_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Apply' , ), 10, (10, (), [ ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 11, (11, (), [ ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Flip' , 'FlipCmd' , ), 13, (13, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'IncrementLeft' , 'Increment' , ), 14, (14, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'IncrementRotation' , 'Increment' , ), 15, (15, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'IncrementTop' , 'Increment' , ), 16, (16, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'PickUp' , ), 17, (17, (), [ ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'RerouteConnections' , ), 18, (18, (), [ ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'ScaleHeight' , 'Factor' , 'RelativeToOriginalSize' , 'fScale' , ), 19, (19, (), [ 
			(4, 1, None, None) , (3, 1, None, None) , (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ScaleWidth' , 'Factor' , 'RelativeToOriginalSize' , 'fScale' , ), 20, (20, (), [ 
			(4, 1, None, None) , (3, 1, None, None) , (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'SetShapesDefaultProperties' , ), 22, (22, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Ungroup' , 'Ungroup' , ), 23, (23, (), [ (16393, 10, None, "IID('{9149347A-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'ZOrder' , 'ZOrderCmd' , ), 24, (24, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Adjustments' , 'Adjustments' , ), 100, (100, (), [ (16393, 10, None, "IID('{9149347C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'AutoShapeType' , 'AutoShapeType' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'AutoShapeType' , 'AutoShapeType' , ), 101, (101, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'BlackWhiteMode' , 'BlackWhiteMode' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'BlackWhiteMode' , 'BlackWhiteMode' , ), 102, (102, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'Callout' , 'Callout' , ), 103, (103, (), [ (16393, 10, None, "IID('{91493485-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionSiteCount' , 'ConnectionSiteCount' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'Connector' , 'Connector' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ConnectorFormat' , 'ConnectorFormat' , ), 106, (106, (), [ (16393, 10, None, "IID('{91493481-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'Fill' , 'Fill' , ), 107, (107, (), [ (16393, 10, None, "IID('{9149347E-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'GroupItems' , 'GroupItems' , ), 108, (108, (), [ (16393, 10, None, "IID('{9149347B-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'Height' , ), 109, (109, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'Height' , ), 109, (109, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'HorizontalFlip' , 'HorizontalFlip' , ), 110, (110, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Left' , 'Left' , ), 111, (111, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( 'Left' , 'Left' , ), 111, (111, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Line' , 'Line' , ), 112, (112, (), [ (16393, 10, None, "IID('{9149347F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( 'LockAspectRatio' , 'LockAspectRatio' , ), 113, (113, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'LockAspectRatio' , 'LockAspectRatio' , ), 113, (113, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 115, (115, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 115, (115, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( 'Nodes' , 'Nodes' , ), 116, (116, (), [ (16393, 10, None, "IID('{91493486-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Rotation' , 'Rotation' , ), 117, (117, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( 'Rotation' , 'Rotation' , ), 117, (117, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'PictureFormat' , 'Picture' , ), 118, (118, (), [ (16393, 10, None, "IID('{9149347D-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
	(( 'Shadow' , 'Shadow' , ), 119, (119, (), [ (16393, 10, None, "IID('{91493480-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'TextEffect' , 'TextEffect' , ), 120, (120, (), [ (16393, 10, None, "IID('{91493482-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 196 , (3, 0, None, None) , 0 , )),
	(( 'TextFrame' , 'TextFrame' , ), 121, (121, (), [ (16393, 10, None, "IID('{91493484-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ThreeD' , 'ThreeD' , ), 122, (122, (), [ (16393, 10, None, "IID('{91493483-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 204 , (3, 0, None, None) , 0 , )),
	(( 'Top' , 'Top' , ), 123, (123, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Top' , 'Top' , ), 123, (123, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 212 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 124, (124, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'VerticalFlip' , 'VerticalFlip' , ), 125, (125, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 220 , (3, 0, None, None) , 0 , )),
	(( 'Vertices' , 'Vertices' , ), 126, (126, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'Visible' , ), 127, (127, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 228 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'Visible' , ), 127, (127, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 128, (128, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 236 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 128, (128, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ZOrderPosition' , 'ZOrderPosition' , ), 129, (129, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 244 , (3, 0, None, None) , 0 , )),
	(( 'OLEFormat' , 'OLEFormat' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{91493488-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'LinkFormat' , 'LinkFormat' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{91493489-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 252 , (3, 0, None, None) , 0 , )),
	(( 'PlaceholderFormat' , 'PlaceholderFormat' , ), 2005, (2005, (), [ (16393, 10, None, "IID('{91493477-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'AnimationSettings' , 'AnimationSettings' , ), 2006, (2006, (), [ (16393, 10, None, "IID('{9149348B-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 260 , (3, 0, None, None) , 0 , )),
	(( 'ActionSettings' , 'ActionSettings' , ), 2007, (2007, (), [ (16393, 10, None, "IID('{9149348C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Tags' , 'Tags' , ), 2008, (2008, (), [ (16393, 10, None, "IID('{914934B9-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 268 , (3, 0, None, None) , 0 , )),
	(( 'Cut' , ), 2009, (2009, (), [ ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Copy' , ), 2010, (2010, (), [ ], 1 , 1 , 4 , 0 , 276 , (3, 0, None, None) , 0 , )),
	(( 'Select' , 'Replace' , ), 2011, (2011, (), [ (3, 49, '-1', None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Duplicate' , 'Duplicate' , ), 2012, (2012, (), [ (16393, 10, None, "IID('{9149347A-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 284 , (3, 0, None, None) , 0 , )),
	(( 'MediaType' , 'MediaType' , ), 2013, (2013, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'HasTextFrame' , 'HasTextFrame' , ), 2014, (2014, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 292 , (3, 0, None, None) , 0 , )),
	(( 'SoundFormat' , 'SoundFormat' , ), 2015, (2015, (), [ (16393, 10, None, "IID('{91493473-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 64 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			(16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 300 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , '_NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 1 , )),
	(( '_Index' , 'Index' , '_Index' , ), 8, (8, (), [ (3, 1, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 308 , (3, 0, None, None) , 1 , )),
	(( 'Count' , 'Count' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Group' , 'Group' , ), 2016, (2016, (), [ (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 316 , (3, 0, None, None) , 0 , )),
	(( 'Regroup' , 'Regroup' , ), 2017, (2017, (), [ (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Align' , 'AlignCmd' , 'RelativeTo' , ), 2018, (2018, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 324 , (3, 0, None, None) , 0 , )),
	(( 'Distribute' , 'DistributeCmd' , 'RelativeTo' , ), 2019, (2019, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'GetPolygonalRepresentation' , 'maxPointsInBuffer' , 'pPoints' , 'numPointsInPolygon' , 'IsOpen' , 
			), 2020, (2020, (), [ (19, 1, None, None) , (16388, 1, None, None) , (16403, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 332 , (3, 0, None, None) , 1 , )),
	(( 'Script' , 'Script' , ), 130, (130, (), [ (16393, 10, None, "IID('{000C0341-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'AlternativeText' , 'AlternativeText' , ), 131, (131, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 340 , (3, 0, None, None) , 0 , )),
	(( 'AlternativeText' , 'AlternativeText' , ), 131, (131, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'HasTable' , 'HasTable' , ), 2021, (2021, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 348 , (3, 0, None, None) , 0 , )),
	(( 'Table' , 'Table' , ), 2022, (2022, (), [ (16393, 10, None, "IID('{914934C3-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'PathName' , 'Filter' , 'ScaleWidth' , 'ScaleHeight' , 
			'ExportMode' , ), 2023, (2023, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 49, '0', None) , 
			(3, 49, '0', None) , (3, 49, '1', None) , ], 1 , 1 , 4 , 0 , 356 , (3, 0, None, None) , 64 , )),
	(( 'HasDiagram' , 'pHasDiagram' , ), 132, (132, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Diagram' , 'Diagram' , ), 133, (133, (), [ (16393, 10, None, "IID('{914934DB-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 364 , (3, 0, None, None) , 0 , )),
	(( 'HasDiagramNode' , 'pHasDiagram' , ), 134, (134, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'DiagramNode' , 'DiagramNode' , ), 135, (135, (), [ (16393, 10, None, "IID('{914934D8-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 372 , (3, 0, None, None) , 0 , )),
	(( 'Child' , 'Child' , ), 136, (136, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'ParentGroup' , 'Parent' , ), 137, (137, (), [ (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 380 , (3, 0, None, None) , 0 , )),
	(( 'CanvasItems' , 'CanvasShapes' , ), 138, (138, (), [ (16393, 10, None, "IID('{914934EC-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 64 , )),
	(( 'Id' , 'pid' , ), 139, (139, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 388 , (3, 0, None, None) , 0 , )),
	(( 'CanvasCropLeft' , 'Increment' , ), 140, (140, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 64 , )),
	(( 'CanvasCropTop' , 'Increment' , ), 141, (141, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 396 , (3, 0, None, None) , 64 , )),
	(( 'CanvasCropRight' , 'Increment' , ), 142, (142, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 64 , )),
	(( 'CanvasCropBottom' , 'Increment' , ), 143, (143, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 404 , (3, 0, None, None) , 64 , )),
	(( 'RTF' , ), 144, (144, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 408 , (3, 0, None, None) , 64 , )),
]

Shapes_vtables_dispatch_ = 1
Shapes_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			(16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , '_NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 1024 , )),
	(( 'AddCallout' , 'Type' , 'Left' , 'Top' , 'Width' , 
			'Height' , 'Callout' , ), 10, (10, (), [ (3, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'AddConnector' , 'Type' , 'BeginX' , 'BeginY' , 'EndX' , 
			'EndY' , 'Connector' , ), 11, (11, (), [ (3, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'AddCurve' , 'SafeArrayOfPoints' , 'Curve' , ), 12, (12, (), [ (12, 1, None, None) , 
			(16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'AddLabel' , 'Orientation' , 'Left' , 'Top' , 'Width' , 
			'Height' , 'Label' , ), 13, (13, (), [ (3, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'AddLine' , 'BeginX' , 'BeginY' , 'EndX' , 'EndY' , 
			'Line' , ), 14, (14, (), [ (4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'AddPicture' , 'FileName' , 'LinkToFile' , 'SaveWithDocument' , 'Left' , 
			'Top' , 'Width' , 'Height' , 'Picture' , ), 15, (15, (), [ 
			(8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , 
			(4, 49, '-1.0', None) , (4, 49, '-1.0', None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'AddPolyline' , 'SafeArrayOfPoints' , 'Polyline' , ), 16, (16, (), [ (12, 1, None, None) , 
			(16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'AddShape' , 'Type' , 'Left' , 'Top' , 'Width' , 
			'Height' , 'Shape' , ), 17, (17, (), [ (3, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'AddTextEffect' , 'PresetTextEffect' , 'Text' , 'FontName' , 'FontSize' , 
			'FontBold' , 'FontItalic' , 'Left' , 'Top' , 'TextEffect' , 
			), 18, (18, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (4, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'AddTextbox' , 'Orientation' , 'Left' , 'Top' , 'Width' , 
			'Height' , 'Textbox' , ), 19, (19, (), [ (3, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'BuildFreeform' , 'EditingType' , 'X1' , 'Y1' , 'FreeformBuilder' , 
			), 20, (20, (), [ (3, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (16393, 10, None, "IID('{91493478-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'SelectAll' , ), 22, (22, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Range' , 'Index' , 'Range' , ), 2003, (2003, (), [ (12, 17, None, None) , 
			(16393, 10, None, "IID('{9149347A-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 1 , 100 , (3, 0, None, None) , 0 , )),
	(( 'HasTitle' , 'HasTitle' , ), 2004, (2004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'AddTitle' , 'Title' , ), 2005, (2005, (), [ (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'Title' , 'Title' , ), 2006, (2006, (), [ (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Placeholders' , 'Placeholders' , ), 2007, (2007, (), [ (16393, 10, None, "IID('{91493476-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'AddOLEObject' , 'Left' , 'Top' , 'Width' , 'Height' , 
			'ClassName' , 'FileName' , 'DisplayAsIcon' , 'IconFileName' , 'IconIndex' , 
			'IconLabel' , 'Link' , 'OLEObject' , ), 2008, (2008, (), [ (4, 49, '0.0', None) , 
			(4, 49, '0.0', None) , (4, 49, '-1.0', None) , (4, 49, '-1.0', None) , (8, 49, "u''", None) , (8, 49, "u''", None) , 
			(3, 49, '0', None) , (8, 49, "u''", None) , (3, 49, '0', None) , (8, 49, "u''", None) , (3, 49, '0', None) , 
			(16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 120 , (3, 32, None, None) , 0 , )),
	(( 'AddComment' , 'Left' , 'Top' , 'Width' , 'Height' , 
			'Comment' , ), 2009, (2009, (), [ (4, 49, '1.25', None) , (4, 49, '1.25', None) , (4, 49, '145.25', None) , 
			(4, 49, '145.25', None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'AddPlaceholder' , 'Type' , 'Left' , 'Top' , 'Width' , 
			'Height' , 'Placeholder' , ), 2010, (2010, (), [ (3, 1, None, None) , (4, 49, '-1.0', None) , 
			(4, 49, '-1.0', None) , (4, 49, '-1.0', None) , (4, 49, '-1.0', None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'AddMediaObject' , 'FileName' , 'Left' , 'Top' , 'Width' , 
			'Height' , 'MediaObject' , ), 2011, (2011, (), [ (8, 1, None, None) , (4, 49, '0.0', None) , 
			(4, 49, '0.0', None) , (4, 49, '-1.0', None) , (4, 49, '-1.0', None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'Paste' , 'Paste' , ), 2012, (2012, (), [ (16393, 10, None, "IID('{9149347A-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'AddTable' , 'NumRows' , 'NumColumns' , 'Left' , 'Top' , 
			'Width' , 'Height' , 'Table' , ), 2013, (2013, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , (4, 49, '-1.0', None) , (4, 49, '-1.0', None) , (4, 49, '-1.0', None) , (4, 49, '-1.0', None) , 
			(16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'PasteSpecial' , 'DataType' , 'DisplayAsIcon' , 'IconFileName' , 'IconIndex' , 
			'IconLabel' , 'Link' , 'PasteSpecial' , ), 2014, (2014, (), [ (3, 49, '0', None) , 
			(3, 49, '0', None) , (8, 49, "u''", None) , (3, 49, '0', None) , (8, 49, "u''", None) , (3, 49, '0', None) , 
			(16393, 10, None, "IID('{9149347A-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 144 , (3, 32, None, None) , 0 , )),
	(( 'AddDiagram' , 'Type' , 'Left' , 'Top' , 'Width' , 
			'Height' , 'Diagram' , ), 23, (23, (), [ (3, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( 'AddCanvas' , 'Left' , 'Top' , 'Width' , 'Height' , 
			'Shape' , ), 25, (25, (), [ (4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 64 , )),
]

SldEvents_vtables_dispatch_ = 0
SldEvents_vtables_ = [
]

SlideRange_vtables_dispatch_ = 1
SlideRange_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Shapes' , 'Shapes' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{91493475-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'HeadersFooters' , 'HeadersFooters' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{91493474-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'SlideShowTransition' , 'SlideShowTransition' , ), 2005, (2005, (), [ (16393, 10, None, "IID('{91493471-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'ColorScheme' , 'ColorScheme' , ), 2006, (2006, (), [ (16393, 10, None, "IID('{9149346F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'ColorScheme' , 'ColorScheme' , ), 2006, (2006, (), [ (9, 1, None, "IID('{9149346F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Background' , 'Background' , ), 2007, (2007, (), [ (16393, 10, None, "IID('{9149347A-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 2008, (2008, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 2008, (2008, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SlideID' , 'SlideID' , ), 2009, (2009, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'PrintSteps' , 'PrintSteps' , ), 2010, (2010, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Select' , ), 2011, (2011, (), [ ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'Cut' , ), 2012, (2012, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Copy' , ), 2013, (2013, (), [ ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'Layout' , 'Layout' , ), 2014, (2014, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Layout' , 'Layout' , ), 2014, (2014, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'Duplicate' , 'Duplicate' , ), 2015, (2015, (), [ (16393, 10, None, "IID('{9149346B-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 2016, (2016, (), [ ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'Tags' , 'Tags' , ), 2017, (2017, (), [ (16393, 10, None, "IID('{914934B9-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SlideIndex' , 'SlideIndex' , ), 2018, (2018, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'SlideNumber' , 'SlideNumber' , ), 2019, (2019, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'DisplayMasterShapes' , 'DisplayMasterShapes' , ), 2020, (2020, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'DisplayMasterShapes' , 'DisplayMasterShapes' , ), 2020, (2020, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'FollowMasterBackground' , 'FollowMasterBackground' , ), 2021, (2021, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'FollowMasterBackground' , 'FollowMasterBackground' , ), 2021, (2021, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'NotesPage' , 'NotesPage' , ), 2022, (2022, (), [ (16393, 10, None, "IID('{9149346B-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'Master' , 'Master' , ), 2023, (2023, (), [ (16393, 10, None, "IID('{9149346C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Hyperlinks' , 'Hyperlinks' , ), 2024, (2024, (), [ (16393, 10, None, "IID('{91493464-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'FileName' , 'FilterName' , 'ScaleWidth' , 'ScaleHeight' , 
			), 2025, (2025, (), [ (8, 1, None, None) , (8, 1, None, None) , (3, 49, '0', None) , (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			(16397, 10, None, "IID('{91493445-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , '_NewEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 1 , )),
	(( '_Index' , 'Index' , '_Index' , ), 10, (10, (), [ (3, 1, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 156 , (3, 0, None, None) , 1 , )),
	(( 'Count' , 'Count' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Scripts' , 'Scripts' , ), 2026, (2026, (), [ (16393, 10, None, "IID('{000C0340-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( 'Comments' , 'Comments' , ), 2028, (2028, (), [ (16393, 10, None, "IID('{914934D4-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Design' , 'Design' , ), 2029, (2029, (), [ (16393, 10, None, "IID('{914934D7-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( 'Design' , 'Design' , ), 2029, (2029, (), [ (9, 1, None, "IID('{914934D7-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'MoveTo' , 'toPos' , ), 2030, (2030, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( 'TimeLine' , 'TimeLine' , ), 2031, (2031, (), [ (16393, 10, None, "IID('{914934DC-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ApplyTemplate' , 'FileName' , ), 2032, (2032, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
]

SlideShowSettings_vtables_dispatch_ = 1
SlideShowSettings_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'PointerColor' , 'PointerColor' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{91493452-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'NamedSlideShows' , 'NamedSlideShows' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{9149345B-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'StartingSlide' , 'StartingSlide' , ), 2005, (2005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'StartingSlide' , 'StartingSlide' , ), 2005, (2005, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'EndingSlide' , 'EndingSlide' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'EndingSlide' , 'EndingSlide' , ), 2006, (2006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'AdvanceMode' , 'AdvanceMode' , ), 2007, (2007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'AdvanceMode' , 'AdvanceMode' , ), 2007, (2007, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Run' , 'Run' , ), 2008, (2008, (), [ (16393, 10, None, "IID('{91493453-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'LoopUntilStopped' , 'LoopUntilStopped' , ), 2009, (2009, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LoopUntilStopped' , 'LoopUntilStopped' , ), 2009, (2009, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'ShowType' , 'ShowType' , ), 2010, (2010, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ShowType' , 'ShowType' , ), 2010, (2010, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'ShowWithNarration' , 'ShowWithNarration' , ), 2011, (2011, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ShowWithNarration' , 'ShowWithNarration' , ), 2011, (2011, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'ShowWithAnimation' , 'ShowWithAnimation' , ), 2012, (2012, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ShowWithAnimation' , 'ShowWithAnimation' , ), 2012, (2012, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'SlideShowName' , 'SlideShowName' , ), 2013, (2013, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SlideShowName' , 'SlideShowName' , ), 2013, (2013, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'RangeType' , 'RangeType' , ), 2014, (2014, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'RangeType' , 'RangeType' , ), 2014, (2014, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'ShowScrollbar' , 'ShowScrollbar' , ), 2015, (2015, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ShowScrollbar' , 'ShowScrollbar' , ), 2015, (2015, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
]

SlideShowTransition_vtables_dispatch_ = 1
SlideShowTransition_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'AdvanceOnClick' , 'AdvanceOnClick' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'AdvanceOnClick' , 'AdvanceOnClick' , ), 2003, (2003, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'AdvanceOnTime' , 'AdvanceOnTime' , ), 2004, (2004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'AdvanceOnTime' , 'AdvanceOnTime' , ), 2004, (2004, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'AdvanceTime' , 'AdvanceTime' , ), 2005, (2005, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'AdvanceTime' , 'AdvanceTime' , ), 2005, (2005, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'EntryEffect' , 'EntryEffect' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'EntryEffect' , 'EntryEffect' , ), 2006, (2006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Hidden' , 'Hidden' , ), 2007, (2007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'Hidden' , 'Hidden' , ), 2007, (2007, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LoopSoundUntilNext' , 'LoopSoundUntilNext' , ), 2008, (2008, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'LoopSoundUntilNext' , 'LoopSoundUntilNext' , ), 2008, (2008, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SoundEffect' , 'SoundEffect' , ), 2009, (2009, (), [ (16393, 10, None, "IID('{91493472-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'Speed' , 'Speed' , ), 2010, (2010, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Speed' , 'Speed' , ), 2010, (2010, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
]

SlideShowView_vtables_dispatch_ = 1
SlideShowView_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Zoom' , 'Zoom' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Slide' , 'Slide' , ), 2004, (2004, (), [ (16397, 10, None, "IID('{91493445-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'PointerType' , 'PointerType' , ), 2005, (2005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'PointerType' , 'PointerType' , ), 2005, (2005, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'State' , 'State' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'State' , 'State' , ), 2006, (2006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'AcceleratorsEnabled' , 'AcceleratorsEnabled' , ), 2007, (2007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'AcceleratorsEnabled' , 'AcceleratorsEnabled' , ), 2007, (2007, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'PresentationElapsedTime' , 'PresentationElapsedTime' , ), 2008, (2008, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'SlideElapsedTime' , 'SlideElapsedTime' , ), 2009, (2009, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SlideElapsedTime' , 'SlideElapsedTime' , ), 2009, (2009, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'LastSlideViewed' , 'LastSlideViewed' , ), 2010, (2010, (), [ (16397, 10, None, "IID('{91493445-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'AdvanceMode' , 'AdvanceMode' , ), 2011, (2011, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'PointerColor' , 'PointerColor' , ), 2012, (2012, (), [ (16393, 10, None, "IID('{91493452-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'IsNamedShow' , 'IsNamedShow' , ), 2013, (2013, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'SlideShowName' , 'SlideShowName' , ), 2014, (2014, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'DrawLine' , 'BeginX' , 'BeginY' , 'EndX' , 'EndY' , 
			), 2015, (2015, (), [ (4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'EraseDrawing' , ), 2016, (2016, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'First' , ), 2017, (2017, (), [ ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'Last' , ), 2018, (2018, (), [ ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Next' , ), 2019, (2019, (), [ ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'Previous' , ), 2020, (2020, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'GotoSlide' , 'Index' , 'ResetSlide' , ), 2021, (2021, (), [ (3, 1, None, None) , 
			(3, 49, '-1', None) , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'GotoNamedShow' , 'SlideShowName' , ), 2022, (2022, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'EndNamedShow' , ), 2023, (2023, (), [ ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'ResetSlideTime' , ), 2024, (2024, (), [ ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Exit' , ), 2025, (2025, (), [ ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'InstallTracker' , 'pTracker' , 'Presenter' , ), 2026, (2026, (), [ (13, 1, None, "IID('{914934BE-5A91-11CF-8700-00AA0060263B}')") , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 64 , )),
	(( 'CurrentShowPosition' , 'CurrentShowPosition' , ), 2027, (2027, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
]

SlideShowWindow_vtables_dispatch_ = 1
SlideShowWindow_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'View' , 'View' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{91493459-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Presentation' , 'Presentation' , ), 2004, (2004, (), [ (16397, 10, None, "IID('{91493444-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'IsFullScreen' , 'IsFullScreen' , ), 2005, (2005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Left' , 'Left' , ), 2006, (2006, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Left' , 'Left' , ), 2006, (2006, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Top' , 'Top' , ), 2007, (2007, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Top' , 'Top' , ), 2007, (2007, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 2008, (2008, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 2008, (2008, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'Height' , ), 2009, (2009, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'Height' , ), 2009, (2009, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'HWND' , 'HWND' , ), 2010, (2010, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 1 , )),
	(( 'Active' , 'Active' , ), 2011, (2011, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'Activate' , ), 2012, (2012, (), [ ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

SlideShowWindows_vtables_dispatch_ = 1
SlideShowWindows_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{91493453-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

Slides_vtables_dispatch_ = 1
Slides_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (12, 1, None, None) , 
			(16397, 10, None, "IID('{91493445-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'FindBySlideID' , 'SlideID' , 'FindBySlideID' , ), 2003, (2003, (), [ (3, 1, None, None) , 
			(16397, 10, None, "IID('{91493445-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Index' , 'Layout' , 'Add' , ), 2004, (2004, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16397, 10, None, "IID('{91493445-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'InsertFromFile' , 'FileName' , 'Index' , 'SlideStart' , 'SlideEnd' , 
			'FromFile' , ), 2005, (2005, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 49, '1', None) , 
			(3, 49, '-1', None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'Range' , 'Index' , 'Range' , ), 2006, (2006, (), [ (12, 17, None, None) , 
			(16393, 10, None, "IID('{9149346B-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 1 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Paste' , 'Index' , 'Paste' , ), 2007, (2007, (), [ (3, 49, '-1', None) , 
			(16393, 10, None, "IID('{9149346B-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
]

SoundEffect_vtables_dispatch_ = 1
SoundEffect_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 2003, (2003, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 2003, (2003, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 2004, (2004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 2004, (2004, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'ImportFromFile' , 'FileName' , ), 2005, (2005, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Play' , ), 2006, (2006, (), [ ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

SoundFormat_vtables_dispatch_ = 1
SoundFormat_vtables_ = [
	(( 'Play' , ), 2000, (2000, (), [ ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'FileName' , ), 2001, (2001, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'FileName' , 'Export' , ), 2002, (2002, (), [ (8, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'SourceFullName' , 'SourceFullName' , ), 2004, (2004, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
]

TabStop_vtables_dispatch_ = 1
TabStop_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 2003, (2003, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'Position' , ), 2004, (2004, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'Position' , ), 2004, (2004, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Clear' , ), 2005, (2005, (), [ ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

TabStops_vtables_dispatch_ = 1
TabStops_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{91493494-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'DefaultSpacing' , 'DefaultSpacing' , ), 2003, (2003, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'DefaultSpacing' , 'DefaultSpacing' , ), 2003, (2003, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Type' , 'Position' , 'Add' , ), 2004, (2004, (), [ 
			(3, 1, None, None) , (4, 1, None, None) , (16393, 10, None, "IID('{91493494-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
]

Table_vtables_dispatch_ = 1
Table_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Columns' , 'Columns' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{914934C4-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Rows' , 'Rows' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{914934C6-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Cell' , 'Row' , 'Column' , 'Cell' , ), 2005, (2005, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{914934C9-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'TableDirection' , 'TableDirection' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'TableDirection' , 'TableDirection' , ), 2006, (2006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'MergeBorders' , ), 2007, (2007, (), [ ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 64 , )),
]

Tags_vtables_dispatch_ = 1
Tags_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Name' , 'Item' , ), 0, (0, (), [ (8, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Name' , 'Value' , ), 2003, (2003, (), [ (8, 1, None, None) , 
			(8, 1, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'Name' , ), 2004, (2004, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'AddBinary' , 'Name' , 'FilePath' , ), 2005, (2005, (), [ (8, 1, None, None) , 
			(8, 1, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 64 , )),
	(( 'BinaryValue' , 'Name' , 'BinaryValue' , ), 2006, (2006, (), [ (8, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 64 , )),
	(( 'Name' , 'Index' , 'Name' , ), 2007, (2007, (), [ (3, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'Index' , 'Value' , ), 2008, (2008, (), [ (3, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

TextEffectFormat_vtables_dispatch_ = 1
TextEffectFormat_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'ToggleVerticalText' , ), 10, (10, (), [ ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Alignment' , 'Alignment' , ), 100, (100, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Alignment' , 'Alignment' , ), 100, (100, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'FontBold' , 'FontBold' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'FontBold' , 'FontBold' , ), 101, (101, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FontItalic' , 'FontItalic' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'FontItalic' , 'FontItalic' , ), 102, (102, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FontName' , 'FontName' , ), 103, (103, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'FontName' , 'FontName' , ), 103, (103, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FontSize' , 'FontSize' , ), 104, (104, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'FontSize' , 'FontSize' , ), 104, (104, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'KernedPairs' , 'KernedPairs' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'KernedPairs' , 'KernedPairs' , ), 105, (105, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'NormalizedHeight' , 'NormalizedHeight' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'NormalizedHeight' , 'NormalizedHeight' , ), 106, (106, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'PresetShape' , 'PresetShape' , ), 107, (107, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'PresetShape' , 'PresetShape' , ), 107, (107, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'PresetTextEffect' , 'Preset' , ), 108, (108, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'PresetTextEffect' , 'Preset' , ), 108, (108, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'RotatedChars' , 'RotatedChars' , ), 109, (109, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'RotatedChars' , 'RotatedChars' , ), 109, (109, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'Text' , ), 110, (110, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'Text' , ), 110, (110, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Tracking' , 'Tracking' , ), 111, (111, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'Tracking' , 'Tracking' , ), 111, (111, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

TextFrame_vtables_dispatch_ = 1
TextFrame_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'MarginBottom' , 'MarginBottom' , ), 100, (100, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'MarginBottom' , 'MarginBottom' , ), 100, (100, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'MarginLeft' , 'MarginLeft' , ), 101, (101, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'MarginLeft' , 'MarginLeft' , ), 101, (101, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'MarginRight' , 'MarginRight' , ), 102, (102, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MarginRight' , 'MarginRight' , ), 102, (102, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'MarginTop' , 'MarginTop' , ), 103, (103, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'MarginTop' , 'MarginTop' , ), 103, (103, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'Orientation' , 'Orientation' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Orientation' , 'Orientation' , ), 104, (104, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'HasText' , 'HasText' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'TextRange' , 'TextRange' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{9149348F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'Ruler' , 'Ruler' , ), 2005, (2005, (), [ (16393, 10, None, "IID('{91493490-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'HorizontalAnchor' , 'HorizontalAnchor' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'HorizontalAnchor' , 'HorizontalAnchor' , ), 2006, (2006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'VerticalAnchor' , 'VerticalAnchor' , ), 2007, (2007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'VerticalAnchor' , 'VerticalAnchor' , ), 2007, (2007, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'AutoSize' , 'AutoSize' , ), 2008, (2008, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'AutoSize' , 'AutoSize' , ), 2008, (2008, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'WordWrap' , 'WordWrap' , ), 2009, (2009, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'WordWrap' , 'WordWrap' , ), 2009, (2009, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DeleteText' , ), 2010, (2010, (), [ ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
]

TextRange_vtables_dispatch_ = 1
TextRange_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'ActionSettings' , 'ActionSettings' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{9149348C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Start' , 'Start' , ), 2004, (2004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Length' , 'Length' , ), 2005, (2005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'BoundLeft' , 'BoundLeft' , ), 2006, (2006, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'BoundTop' , 'BoundTop' , ), 2007, (2007, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'BoundWidth' , 'BoundWidth' , ), 2008, (2008, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'BoundHeight' , 'BoundHeight' , ), 2009, (2009, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Paragraphs' , 'Start' , 'Length' , 'Paragraphs' , ), 2010, (2010, (), [ 
			(3, 49, '-1', None) , (3, 49, '-1', None) , (16393, 10, None, "IID('{9149348F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'Sentences' , 'Start' , 'Length' , 'Sentences' , ), 2011, (2011, (), [ 
			(3, 49, '-1', None) , (3, 49, '-1', None) , (16393, 10, None, "IID('{9149348F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Words' , 'Start' , 'Length' , 'Words' , ), 2012, (2012, (), [ 
			(3, 49, '-1', None) , (3, 49, '-1', None) , (16393, 10, None, "IID('{9149348F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'Characters' , 'Start' , 'Length' , 'Characters' , ), 2013, (2013, (), [ 
			(3, 49, '-1', None) , (3, 49, '-1', None) , (16393, 10, None, "IID('{9149348F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Lines' , 'Start' , 'Length' , 'Lines' , ), 2014, (2014, (), [ 
			(3, 49, '-1', None) , (3, 49, '-1', None) , (16393, 10, None, "IID('{9149348F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'Runs' , 'Start' , 'Length' , 'Runs' , ), 2015, (2015, (), [ 
			(3, 49, '-1', None) , (3, 49, '-1', None) , (16393, 10, None, "IID('{9149348F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'TrimText' , 'TrimText' , ), 2016, (2016, (), [ (16393, 10, None, "IID('{9149348F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'Text' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'Text' , ), 0, (0, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'InsertAfter' , 'NewText' , 'After' , ), 2017, (2017, (), [ (8, 49, "u''", None) , 
			(16393, 10, None, "IID('{9149348F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 32, None, None) , 0 , )),
	(( 'InsertBefore' , 'NewText' , 'Before' , ), 2018, (2018, (), [ (8, 49, "u''", None) , 
			(16393, 10, None, "IID('{9149348F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 116 , (3, 32, None, None) , 0 , )),
	(( 'InsertDateTime' , 'DateTimeFormat' , 'InsertAsField' , 'DateTime' , ), 2019, (2019, (), [ 
			(3, 1, None, None) , (3, 49, '0', None) , (16393, 10, None, "IID('{9149348F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InsertSlideNumber' , 'SlideNumber' , ), 2020, (2020, (), [ (16393, 10, None, "IID('{9149348F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'InsertSymbol' , 'FontName' , 'CharNumber' , 'Unicode' , 'Symbol' , 
			), 2021, (2021, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 49, '0', None) , (16393, 10, None, "IID('{9149348F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Font' , 'Font' , ), 2022, (2022, (), [ (16393, 10, None, "IID('{91493495-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'ParagraphFormat' , 'ParagraphFormat' , ), 2023, (2023, (), [ (16393, 10, None, "IID('{91493496-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'IndentLevel' , 'IndentLevel' , ), 2024, (2024, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'IndentLevel' , 'IndentLevel' , ), 2024, (2024, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Select' , ), 2025, (2025, (), [ ], 1 , 1 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( 'Cut' , ), 2026, (2026, (), [ ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Copy' , ), 2027, (2027, (), [ ], 1 , 1 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 2028, (2028, (), [ ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Paste' , 'Paste' , ), 2029, (2029, (), [ (16393, 10, None, "IID('{9149348F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( 'ChangeCase' , 'Type' , ), 2030, (2030, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'AddPeriods' , ), 2031, (2031, (), [ ], 1 , 1 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( 'RemovePeriods' , ), 2032, (2032, (), [ ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Find' , 'FindWhat' , 'After' , 'MatchCase' , 'WholeWords' , 
			'Find' , ), 2033, (2033, (), [ (8, 1, None, None) , (3, 49, '0', None) , (3, 49, '0', None) , 
			(3, 49, '0', None) , (16393, 10, None, "IID('{9149348F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( 'Replace' , 'FindWhat' , 'ReplaceWhat' , 'After' , 'MatchCase' , 
			'WholeWords' , 'Replace' , ), 2034, (2034, (), [ (8, 1, None, None) , (8, 1, None, None) , 
			(3, 49, '0', None) , (3, 49, '0', None) , (3, 49, '0', None) , (16393, 10, None, "IID('{9149348F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'RotatedBounds' , 'X1' , 'Y1' , 'X2' , 'Y2' , 
			'X3' , 'Y3' , 'x4' , 'y4' , ), 2035, (2035, (), [ 
			(16388, 2, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , 
			(16388, 2, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , ], 1 , 1 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
	(( 'LanguageID' , 'LanguageID' , ), 2036, (2036, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'LanguageID' , 'LanguageID' , ), 2036, (2036, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 196 , (3, 0, None, None) , 0 , )),
	(( 'RtlRun' , ), 2037, (2037, (), [ ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'LtrRun' , ), 2038, (2038, (), [ ], 1 , 1 , 4 , 0 , 204 , (3, 0, None, None) , 0 , )),
	(( 'PasteSpecial' , 'DataType' , 'DisplayAsIcon' , 'IconFileName' , 'IconIndex' , 
			'IconLabel' , 'Link' , 'PasteSpecial' , ), 2039, (2039, (), [ (3, 49, '0', None) , 
			(3, 49, '0', None) , (8, 49, "u''", None) , (3, 49, '0', None) , (8, 49, "u''", None) , (3, 49, '0', None) , 
			(16393, 10, None, "IID('{9149348F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 208 , (3, 32, None, None) , 0 , )),
]

TextStyle_vtables_dispatch_ = 1
TextStyle_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Ruler' , 'Ruler' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{91493490-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'TextFrame' , 'TextFrame' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{91493484-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Levels' , 'Levels' , ), 2005, (2005, (), [ (16393, 10, None, "IID('{9149349A-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
]

TextStyleLevel_vtables_dispatch_ = 1
TextStyleLevel_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'ParagraphFormat' , 'ParagraphFormat' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{91493496-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Font' , 'Font' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{91493495-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
]

TextStyleLevels_vtables_dispatch_ = 1
TextStyleLevels_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Level' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{9149349B-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

TextStyles_vtables_dispatch_ = 1
TextStyles_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Type' , 'Item' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{91493499-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

ThreeDFormat_vtables_dispatch_ = 1
ThreeDFormat_vtables_ = [
	(( 'Application' , 'ppidisp' , ), 2001, (2001, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'plCreator' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'IncrementRotationX' , 'Increment' , ), 10, (10, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'IncrementRotationY' , 'Increment' , ), 11, (11, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'ResetRotation' , ), 12, (12, (), [ ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'SetThreeDFormat' , 'PresetThreeDFormat' , ), 13, (13, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'SetExtrusionDirection' , 'PresetExtrusionDirection' , ), 14, (14, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Depth' , 'Depth' , ), 100, (100, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'Depth' , 'Depth' , ), 100, (100, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ExtrusionColor' , 'ExtrusionColor' , ), 101, (101, (), [ (16393, 10, None, "IID('{91493452-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'ExtrusionColorType' , 'ExtrusionColorType' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ExtrusionColorType' , 'ExtrusionColorType' , ), 102, (102, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'Perspective' , 'Perspective' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Perspective' , 'Perspective' , ), 103, (103, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'PresetExtrusionDirection' , 'PresetExtrusionDirection' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'PresetLightingDirection' , 'PresetLightingDirection' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'PresetLightingDirection' , 'PresetLightingDirection' , ), 105, (105, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'PresetLightingSoftness' , 'PresetLightingSoftness' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'PresetLightingSoftness' , 'PresetLightingSoftness' , ), 106, (106, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'PresetMaterial' , 'PresetMaterial' , ), 107, (107, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'PresetMaterial' , 'PresetMaterial' , ), 107, (107, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'PresetThreeDFormat' , 'PresetThreeDFormat' , ), 108, (108, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'RotationX' , 'RotationX' , ), 109, (109, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'RotationX' , 'RotationX' , ), 109, (109, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'RotationY' , 'RotationY' , ), 110, (110, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'RotationY' , 'RotationY' , ), 110, (110, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'Visible' , ), 111, (111, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'Visible' , ), 111, (111, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
]

TimeLine_vtables_dispatch_ = 1
TimeLine_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'MainSequence' , 'MainSequence' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{914934DE-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'InteractiveSequences' , 'InteractiveSequences' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{914934DD-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
]

Timing_vtables_dispatch_ = 1
Timing_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Duration' , 'Duration' , ), 2003, (2003, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Duration' , 'Duration' , ), 2003, (2003, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'TriggerType' , 'TriggerType' , ), 2004, (2004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'TriggerType' , 'TriggerType' , ), 2004, (2004, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'TriggerDelayTime' , 'TriggerDelayTime' , ), 2005, (2005, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'TriggerDelayTime' , 'TriggerDelayTime' , ), 2005, (2005, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'TriggerShape' , 'TriggerShape' , ), 2006, (2006, (), [ (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'TriggerShape' , 'TriggerShape' , ), 2006, (2006, (), [ (9, 1, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'RepeatCount' , 'RepeatCount' , ), 2007, (2007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'RepeatCount' , 'RepeatCount' , ), 2007, (2007, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'RepeatDuration' , 'RepeatDuration' , ), 2008, (2008, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'RepeatDuration' , 'RepeatDuration' , ), 2008, (2008, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Speed' , 'Speed' , ), 2009, (2009, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'Speed' , 'Speed' , ), 2009, (2009, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Accelerate' , 'Accelerate' , ), 2010, (2010, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'Accelerate' , 'Accelerate' , ), 2010, (2010, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Decelerate' , 'Decelerate' , ), 2011, (2011, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'Decelerate' , 'Decelerate' , ), 2011, (2011, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'AutoReverse' , 'AutoReverse' , ), 2012, (2012, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'AutoReverse' , 'AutoReverse' , ), 2012, (2012, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'SmoothStart' , 'SmoothStart' , ), 2013, (2013, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'SmoothStart' , 'SmoothStart' , ), 2013, (2013, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SmoothEnd' , 'SmoothEnd' , ), 2014, (2014, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'SmoothEnd' , 'SmoothEnd' , ), 2014, (2014, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'RewindAtEnd' , 'RewindAtEnd' , ), 2015, (2015, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'RewindAtEnd' , 'RewindAtEnd' , ), 2015, (2015, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Restart' , 'Restart' , ), 2016, (2016, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'Restart' , 'Restart' , ), 2016, (2016, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

View_vtables_dispatch_ = 1
View_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Zoom' , 'Zoom' , ), 2004, (2004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Zoom' , 'Zoom' , ), 2004, (2004, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Paste' , ), 2005, (2005, (), [ ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Slide' , 'Slide' , ), 2006, (2006, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Slide' , 'Slide' , ), 2006, (2006, (), [ (9, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GotoSlide' , 'Index' , ), 2007, (2007, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'DisplaySlideMiniature' , 'DisplaySlideMiniature' , ), 2008, (2008, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'DisplaySlideMiniature' , 'DisplaySlideMiniature' , ), 2008, (2008, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'ZoomToFit' , 'ZoomToFit' , ), 2009, (2009, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ZoomToFit' , 'ZoomToFit' , ), 2009, (2009, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'PasteSpecial' , 'DataType' , 'DisplayAsIcon' , 'IconFileName' , 'IconIndex' , 
			'IconLabel' , 'Link' , ), 2010, (2010, (), [ (3, 49, '0', None) , (3, 49, '0', None) , 
			(8, 49, "u''", None) , (3, 49, '0', None) , (8, 49, "u''", None) , (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 80 , (3, 32, None, None) , 0 , )),
	(( 'PrintOptions' , 'PrintOptions' , ), 2011, (2011, (), [ (16393, 10, None, "IID('{9149345D-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'PrintOut' , 'From' , 'To' , 'PrintToFile' , 'Copies' , 
			'Collate' , ), 2012, (2012, (), [ (3, 49, '-1', None) , (3, 49, '-1', None) , (8, 49, "u''", None) , 
			(3, 49, '0', None) , (3, 49, '-99', None) , ], 1 , 1 , 4 , 0 , 88 , (3, 32, None, None) , 0 , )),
]

WebOptions_vtables_dispatch_ = 1
WebOptions_vtables_ = [
	(( 'IncludeNavigation' , 'IncludeNavigation' , ), 2001, (2001, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'IncludeNavigation' , 'IncludeNavigation' , ), 2001, (2001, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'FrameColors' , 'FrameColors' , ), 2002, (2002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'FrameColors' , 'FrameColors' , ), 2002, (2002, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'ResizeGraphics' , 'ResizeGraphics' , ), 2003, (2003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'ResizeGraphics' , 'ResizeGraphics' , ), 2003, (2003, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'ShowSlideAnimation' , 'ShowSlideAnimation' , ), 2004, (2004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'ShowSlideAnimation' , 'ShowSlideAnimation' , ), 2004, (2004, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'OrganizeInFolder' , 'OrganizeInFolder' , ), 2005, (2005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'OrganizeInFolder' , 'OrganizeInFolder' , ), 2005, (2005, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseLongFileNames' , 'UseLongFileNames' , ), 2006, (2006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'UseLongFileNames' , 'UseLongFileNames' , ), 2006, (2006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'RelyOnVML' , 'RelyOnVML' , ), 2007, (2007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'RelyOnVML' , 'RelyOnVML' , ), 2007, (2007, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'AllowPNG' , 'AllowPNG' , ), 2008, (2008, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'AllowPNG' , 'AllowPNG' , ), 2008, (2008, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ScreenSize' , 'ScreenSize' , ), 2009, (2009, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'ScreenSize' , 'ScreenSize' , ), 2009, (2009, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Encoding' , 'Encoding' , ), 2010, (2010, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'Encoding' , 'Encoding' , ), 2010, (2010, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'FolderSuffix' , 'FolderSuffix' , ), 2011, (2011, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'UseDefaultFolderSuffix' , ), 2012, (2012, (), [ ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'TargetBrowser' , 'TargetBrowser' , ), 2013, (2013, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'TargetBrowser' , 'TargetBrowser' , ), 2013, (2013, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'HTMLVersion' , 'HTMLVersion' , ), 2014, (2014, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'HTMLVersion' , 'HTMLVersion' , ), 2014, (2014, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

_Application_vtables_dispatch_ = 1
_Application_vtables_ = [
	(( 'Presentations' , 'Presentations' , ), 2001, (2001, (), [ (16393, 10, None, "IID('{91493462-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Windows' , 'Windows' , ), 2002, (2002, (), [ (16393, 10, None, "IID('{91493455-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Dialogs' , 'Dialogs' , ), 2003, (2003, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 64 , )),
	(( 'ActiveWindow' , 'ActiveWindow' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{91493457-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'ActivePresentation' , 'ActivePresentation' , ), 2005, (2005, (), [ (16397, 10, None, "IID('{91493444-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'SlideShowWindows' , 'SlideShowWindows' , ), 2006, (2006, (), [ (16393, 10, None, "IID('{91493456-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'CommandBars' , 'CommandBars' , ), 2007, (2007, (), [ (16397, 10, None, "IID('{55F88893-7708-11D1-ACEB-006008961DA5}')") , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Path' , 'Path' , ), 2008, (2008, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'Caption' , 'Caption' , ), 2009, (2009, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Caption' , 'Caption' , ), 2009, (2009, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'Assistant' , 'Assistant' , ), 2010, (2010, (), [ (16393, 10, None, "IID('{000C0322-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FileSearch' , 'FileSearch' , ), 2011, (2011, (), [ (16393, 10, None, "IID('{000C0332-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'FileFind' , 'FileFind' , ), 2012, (2012, (), [ (16393, 10, None, "IID('{000C0337-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Build' , 'Build' , ), 2013, (2013, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'Version' , 'Version' , ), 2014, (2014, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'OperatingSystem' , 'OperatingSystem' , ), 2015, (2015, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'ActivePrinter' , 'ActivePrinter' , ), 2016, (2016, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Creator' , 'Creator' , ), 2017, (2017, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'AddIns' , 'AddIns' , ), 2018, (2018, (), [ (16393, 10, None, "IID('{91493460-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'VBE' , 'VBE' , ), 2019, (2019, (), [ (16393, 10, None, "IID('{0002E166-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'Help' , 'HelpFile' , 'ContextID' , ), 2020, (2020, (), [ (8, 49, "u'vbapp10.chm'", None) , 
			(3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 112 , (3, 32, None, None) , 0 , )),
	(( 'Quit' , ), 2021, (2021, (), [ ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'Run' , 'MacroName' , 'safeArrayOfParams' , 'Run' , ), 2022, (2022, (), [ 
			(8, 1, None, None) , (24588, 1, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , -1 , 120 , (3, 0, None, None) , 0 , )),
	(( 'PPFileDialog' , 'Type' , 'PPFileDialog' , ), 2023, (2023, (), [ (3, 1, None, None) , 
			(16397, 10, None, None) , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 64 , )),
	(( 'LaunchSpelling' , 'pWindow' , ), 2024, (2024, (), [ (9, 1, None, "IID('{91493457-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 1 , )),
	(( 'Left' , 'Left' , ), 2025, (2025, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'Left' , 'Left' , ), 2025, (2025, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Top' , 'Top' , ), 2026, (2026, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'Top' , 'Top' , ), 2026, (2026, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 2027, (2027, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 2027, (2027, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'Height' , ), 2028, (2028, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'Height' , ), 2028, (2028, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'WindowState' , 'WindowState' , ), 2029, (2029, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( 'WindowState' , 'WindowState' , ), 2029, (2029, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'Visible' , ), 2030, (2030, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'Visible' , ), 2030, (2030, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'HWND' , 'HWND' , ), 2031, (2031, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 180 , (3, 0, None, None) , 1 , )),
	(( 'Active' , 'Active' , ), 2032, (2032, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Activate' , ), 2033, (2033, (), [ ], 1 , 1 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
	(( 'AnswerWizard' , 'AnswerWizard' , ), 2034, (2034, (), [ (16393, 10, None, "IID('{000C0360-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'COMAddIns' , 'COMAddIns' , ), 2035, (2035, (), [ (16393, 10, None, "IID('{000C0339-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 196 , (3, 0, None, None) , 0 , )),
	(( 'ProductCode' , 'ProductCode' , ), 2036, (2036, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'DefaultWebOptions' , 'DefaultWebOptions' , ), 2037, (2037, (), [ (16393, 10, None, "IID('{914934CD-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 204 , (3, 0, None, None) , 0 , )),
	(( 'LanguageSettings' , 'LanguageSettings' , ), 2038, (2038, (), [ (16393, 10, None, "IID('{000C0353-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'MsoDebugOptions' , 'MsoDebugOptions' , ), 2039, (2039, (), [ (16393, 10, None, "IID('{000C035A-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 212 , (3, 0, None, None) , 64 , )),
	(( 'ShowWindowsInTaskbar' , 'ShowWindowsInTaskbar' , ), 2040, (2040, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ShowWindowsInTaskbar' , 'ShowWindowsInTaskbar' , ), 2040, (2040, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 220 , (3, 0, None, None) , 0 , )),
	(( 'Marker' , 'Marker' , ), 2041, (2041, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 64 , )),
	(( 'FeatureInstall' , 'FeatureInstall' , ), 2042, (2042, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 228 , (3, 0, None, None) , 0 , )),
	(( 'FeatureInstall' , 'FeatureInstall' , ), 2042, (2042, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'GetOptionFlag' , 'Option' , 'Persist' , 'GetOptionFlag' , ), 2043, (2043, (), [ 
			(3, 1, None, None) , (11, 49, 'False', None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 236 , (3, 0, None, None) , 64 , )),
	(( 'SetOptionFlag' , 'Option' , 'State' , 'Persist' , ), 2044, (2044, (), [ 
			(3, 1, None, None) , (11, 1, None, None) , (11, 49, 'False', None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 64 , )),
	(( 'FileDialog' , 'Type' , 'FileDialog' , ), 2045, (2045, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{000C0362-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 244 , (3, 0, None, None) , 0 , )),
	(( 'DisplayGridLines' , 'DisplayGridLines' , ), 2046, (2046, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'DisplayGridLines' , 'DisplayGridLines' , ), 2046, (2046, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 252 , (3, 0, None, None) , 0 , )),
	(( 'AutomationSecurity' , 'AutomationSecurity' , ), 2047, (2047, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'AutomationSecurity' , 'AutomationSecurity' , ), 2047, (2047, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 260 , (3, 0, None, None) , 0 , )),
	(( 'NewPresentation' , 'NewPresentation' , ), 2048, (2048, (), [ (16393, 10, None, "IID('{000C0936-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'DisplayAlerts' , 'DisplayAlerts' , ), 2049, (2049, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 268 , (3, 0, None, None) , 0 , )),
	(( 'DisplayAlerts' , 'DisplayAlerts' , ), 2049, (2049, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ShowStartupDialog' , 'ShowStartupDialog' , ), 2050, (2050, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 276 , (3, 0, None, None) , 0 , )),
	(( 'ShowStartupDialog' , 'ShowStartupDialog' , ), 2050, (2050, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'SetPerfMarker' , 'Marker' , ), 2051, (2051, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 284 , (3, 0, None, None) , 64 , )),
	(( 'AutoCorrect' , 'AutoCorrect' , ), 2052, (2052, (), [ (16393, 10, None, "IID('{914934ED-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Options' , 'Options' , ), 2053, (2053, (), [ (16393, 10, None, "IID('{914934EE-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 292 , (3, 0, None, None) , 0 , )),
]

_Global_vtables_dispatch_ = 1
_Global_vtables_ = [
	(( 'ActivePresentation' , 'ActivePresentation' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493444-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'ActiveWindow' , 'ActiveWindow' , ), 2002, (2002, (), [ (16393, 10, None, "IID('{91493457-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'AddIns' , 'AddIns' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{91493460-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'Application' , ), 2004, (2004, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Assistant' , 'Assistant' , ), 2005, (2005, (), [ (16393, 10, None, "IID('{000C0322-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Dialogs' , 'Dialogs' , ), 2006, (2006, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 64 , )),
	(( 'Presentations' , 'Presentations' , ), 2007, (2007, (), [ (16393, 10, None, "IID('{91493462-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'SlideShowWindows' , 'SlideShowWindows' , ), 2008, (2008, (), [ (16393, 10, None, "IID('{91493456-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Windows' , 'Windows' , ), 2009, (2009, (), [ (16393, 10, None, "IID('{91493455-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'CommandBars' , 'CommandBars' , ), 2010, (2010, (), [ (16397, 10, None, "IID('{55F88893-7708-11D1-ACEB-006008961DA5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'AnswerWizard' , 'AnswerWizard' , ), 2011, (2011, (), [ (16393, 10, None, "IID('{000C0360-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
]

_Master_vtables_dispatch_ = 1
_Master_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Shapes' , 'Shapes' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{91493475-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'HeadersFooters' , 'HeadersFooters' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{91493474-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'ColorScheme' , 'ColorScheme' , ), 2005, (2005, (), [ (16393, 10, None, "IID('{9149346F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'ColorScheme' , 'ColorScheme' , ), 2005, (2005, (), [ (9, 1, None, "IID('{9149346F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'Background' , 'Background' , ), 2006, (2006, (), [ (16393, 10, None, "IID('{9149347A-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 2007, (2007, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 2007, (2007, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 2008, (2008, (), [ ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'Height' , ), 2009, (2009, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 2010, (2010, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'TextStyles' , 'TextStyles' , ), 2011, (2011, (), [ (16393, 10, None, "IID('{91493498-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'Hyperlinks' , 'Hyperlinks' , ), 2012, (2012, (), [ (16393, 10, None, "IID('{91493464-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Scripts' , 'Scripts' , ), 2013, (2013, (), [ (16393, 10, None, "IID('{000C0340-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'Design' , 'Design' , ), 2014, (2014, (), [ (16393, 10, None, "IID('{914934D7-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'TimeLine' , 'TimeLine' , ), 2015, (2015, (), [ (16393, 10, None, "IID('{914934DC-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'SlideShowTransition' , 'SlideShowTransition' , ), 2016, (2016, (), [ (16393, 10, None, "IID('{91493471-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

_PowerRex_vtables_dispatch_ = 1
_PowerRex_vtables_ = [
	(( 'OnAsfEncoderEvent' , 'erorCode' , 'bstrErrorDesc' , ), 2001, (2001, (), [ (12, 1, None, None) , 
			(12, 1, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 64 , )),
]

_Presentation_vtables_dispatch_ = 1
_Presentation_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'SlideMaster' , 'SlideMaster' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{9149346C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'TitleMaster' , 'TitleMaster' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{9149346C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'HasTitleMaster' , 'HasTitleMaster' , ), 2005, (2005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'AddTitleMaster' , 'TitleMaster' , ), 2006, (2006, (), [ (16393, 10, None, "IID('{9149346C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'ApplyTemplate' , 'FileName' , ), 2007, (2007, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'TemplateName' , 'TemplateName' , ), 2008, (2008, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'NotesMaster' , 'NotesMaster' , ), 2009, (2009, (), [ (16393, 10, None, "IID('{9149346C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'HandoutMaster' , 'HandoutMaster' , ), 2010, (2010, (), [ (16393, 10, None, "IID('{9149346C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Slides' , 'Slides' , ), 2011, (2011, (), [ (16393, 10, None, "IID('{91493469-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'PageSetup' , 'PageSetup' , ), 2012, (2012, (), [ (16393, 10, None, "IID('{91493466-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ColorSchemes' , 'ColorSchemes' , ), 2013, (2013, (), [ (16393, 10, None, "IID('{9149346E-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'ExtraColors' , 'ExtraColors' , ), 2014, (2014, (), [ (16393, 10, None, "IID('{91493468-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SlideShowSettings' , 'SlideShowSettings' , ), 2015, (2015, (), [ (16393, 10, None, "IID('{9149345A-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'Fonts' , 'Fonts' , ), 2016, (2016, (), [ (16393, 10, None, "IID('{91493467-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Windows' , 'Windows' , ), 2017, (2017, (), [ (16393, 10, None, "IID('{91493455-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'Tags' , 'Tags' , ), 2018, (2018, (), [ (16393, 10, None, "IID('{914934B9-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'DefaultShape' , 'DefaultShape' , ), 2019, (2019, (), [ (16393, 10, None, "IID('{91493479-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'BuiltInDocumentProperties' , 'BuiltInDocumentProperties' , ), 2020, (2020, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'CustomDocumentProperties' , 'CustomDocumentProperties' , ), 2021, (2021, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'VBProject' , 'VBProject' , ), 2022, (2022, (), [ (16397, 10, None, "IID('{0002E169-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ReadOnly' , 'ReadOnly' , ), 2023, (2023, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'FullName' , 'FullName' , ), 2024, (2024, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 2025, (2025, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'Path' , 'Path' , ), 2026, (2026, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Saved' , 'Saved' , ), 2027, (2027, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'Saved' , 'Saved' , ), 2027, (2027, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'LayoutDirection' , 'LayoutDirection' , ), 2028, (2028, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'LayoutDirection' , 'LayoutDirection' , ), 2028, (2028, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'NewWindow' , 'NewWindow' , ), 2029, (2029, (), [ (16393, 10, None, "IID('{91493457-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( 'FollowHyperlink' , 'Address' , 'SubAddress' , 'NewWindow' , 'AddHistory' , 
			'ExtraInfo' , 'Method' , 'HeaderInfo' , ), 2030, (2030, (), [ (8, 1, None, None) , 
			(8, 49, "u''", None) , (11, 49, 'False', None) , (11, 49, 'True', None) , (8, 49, "u''", None) , (3, 49, '0', None) , 
			(8, 49, "u''", None) , ], 1 , 1 , 4 , 0 , 152 , (3, 32, None, None) , 0 , )),
	(( 'AddToFavorites' , ), 2031, (2031, (), [ ], 1 , 1 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( 'Unused' , ), 2032, (2032, (), [ ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 1 , )),
	(( 'PrintOptions' , 'PrintOptions' , ), 2033, (2033, (), [ (16393, 10, None, "IID('{9149345D-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( 'PrintOut' , 'From' , 'To' , 'PrintToFile' , 'Copies' , 
			'Collate' , ), 2034, (2034, (), [ (3, 49, '-1', None) , (3, 49, '-1', None) , (8, 49, "u''", None) , 
			(3, 49, '0', None) , (3, 49, '-99', None) , ], 1 , 1 , 4 , 0 , 168 , (3, 32, None, None) , 0 , )),
	(( 'Save' , ), 2035, (2035, (), [ ], 1 , 1 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( 'SaveAs' , 'FileName' , 'FileFormat' , 'EmbedTrueTypeFonts' , ), 2036, (2036, (), [ 
			(8, 1, None, None) , (3, 49, '1', None) , (3, 49, '-2', None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'SaveCopyAs' , 'FileName' , 'FileFormat' , 'EmbedTrueTypeFonts' , ), 2037, (2037, (), [ 
			(8, 1, None, None) , (3, 49, '11', None) , (3, 49, '-2', None) , ], 1 , 1 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'Path' , 'FilterName' , 'ScaleWidth' , 'ScaleHeight' , 
			), 2038, (2038, (), [ (8, 1, None, None) , (8, 1, None, None) , (3, 49, '0', None) , (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Close' , ), 2039, (2039, (), [ ], 1 , 1 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
	(( 'SetUndoText' , 'Text' , ), 2040, (2040, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 64 , )),
	(( 'Container' , 'Container' , ), 2041, (2041, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 196 , (3, 0, None, None) , 0 , )),
	(( 'DisplayComments' , 'DisplayComments' , ), 2042, (2042, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'DisplayComments' , 'DisplayComments' , ), 2042, (2042, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 204 , (3, 0, None, None) , 0 , )),
	(( 'FarEastLineBreakLevel' , 'FarEastLineBreakLevel' , ), 2043, (2043, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'FarEastLineBreakLevel' , 'FarEastLineBreakLevel' , ), 2043, (2043, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 212 , (3, 0, None, None) , 0 , )),
	(( 'NoLineBreakBefore' , 'NoLineBreakBefore' , ), 2044, (2044, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'NoLineBreakBefore' , 'NoLineBreakBefore' , ), 2044, (2044, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 220 , (3, 0, None, None) , 0 , )),
	(( 'NoLineBreakAfter' , 'NoLineBreakAfter' , ), 2045, (2045, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'NoLineBreakAfter' , 'NoLineBreakAfter' , ), 2045, (2045, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 228 , (3, 0, None, None) , 0 , )),
	(( 'UpdateLinks' , ), 2046, (2046, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'SlideShowWindow' , 'SlideShowWindow' , ), 2047, (2047, (), [ (16393, 10, None, "IID('{91493453-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 236 , (3, 0, None, None) , 0 , )),
	(( 'FarEastLineBreakLanguage' , 'FarEastLineBreakLanguage' , ), 2048, (2048, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'FarEastLineBreakLanguage' , 'FarEastLineBreakLanguage' , ), 2048, (2048, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 244 , (3, 0, None, None) , 0 , )),
	(( 'WebPagePreview' , ), 2049, (2049, (), [ ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'DefaultLanguageID' , 'DefaultLanguageID' , ), 2050, (2050, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 252 , (3, 0, None, None) , 0 , )),
	(( 'DefaultLanguageID' , 'DefaultLanguageID' , ), 2050, (2050, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'CommandBars' , 'CommandBars' , ), 2051, (2051, (), [ (16397, 10, None, "IID('{55F88893-7708-11D1-ACEB-006008961DA5}')") , ], 1 , 2 , 4 , 0 , 260 , (3, 0, None, None) , 0 , )),
	(( 'PublishObjects' , 'PublishObjects' , ), 2052, (2052, (), [ (16393, 10, None, "IID('{914934CF-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'WebOptions' , 'WebOptions' , ), 2053, (2053, (), [ (16393, 10, None, "IID('{914934CE-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 268 , (3, 0, None, None) , 0 , )),
	(( 'HTMLProject' , 'HTMLProject' , ), 2054, (2054, (), [ (16393, 10, None, "IID('{000C0356-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ReloadAs' , 'cp' , ), 2055, (2055, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 276 , (3, 0, None, None) , 0 , )),
	(( 'MakeIntoTemplate' , 'IsDesignTemplate' , ), 2056, (2056, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 64 , )),
	(( 'EnvelopeVisible' , 'EnvelopeVisible' , ), 2057, (2057, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 284 , (3, 0, None, None) , 0 , )),
	(( 'EnvelopeVisible' , 'EnvelopeVisible' , ), 2057, (2057, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'sblt' , 's' , ), 2058, (2058, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 292 , (3, 0, None, None) , 64 , )),
	(( 'VBASigned' , 'VBASigned' , ), 2059, (2059, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'SnapToGrid' , 'SnapToGrid' , ), 2061, (2061, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 300 , (3, 0, None, None) , 0 , )),
	(( 'SnapToGrid' , 'SnapToGrid' , ), 2061, (2061, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'GridDistance' , 'GridDistance' , ), 2062, (2062, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 308 , (3, 0, None, None) , 0 , )),
	(( 'GridDistance' , 'GridDistance' , ), 2062, (2062, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Designs' , 'Designs' , ), 2063, (2063, (), [ (16393, 10, None, "IID('{914934D6-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 316 , (3, 0, None, None) , 0 , )),
	(( 'Merge' , 'Path' , ), 2064, (2064, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'CheckIn' , 'SaveChanges' , 'Comments' , 'MakePublic' , ), 2065, (2065, (), [ 
			(11, 49, 'True', None) , (12, 17, None, None) , (12, 17, None, None) , ], 1 , 1 , 4 , 2 , 324 , (3, 0, None, None) , 0 , )),
	(( 'CanCheckIn' , 'CanCheckIn' , ), 2066, (2066, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Signatures' , 'Signatures' , ), 2067, (2067, (), [ (16393, 10, None, "IID('{000C0410-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 332 , (3, 0, None, None) , 0 , )),
	(( 'RemovePersonalInformation' , 'RemovePersonalInformation' , ), 2068, (2068, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'RemovePersonalInformation' , 'RemovePersonalInformation' , ), 2068, (2068, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 340 , (3, 0, None, None) , 0 , )),
	(( 'SendForReview' , 'Recipients' , 'Subject' , 'ShowMessage' , 'IncludeAttachment' , 
			), 2069, (2069, (), [ (8, 49, "u''", None) , (8, 49, "u''", None) , (11, 49, 'True', None) , (12, 17, None, None) , ], 1 , 1 , 4 , 1 , 344 , (3, 32, None, None) , 0 , )),
	(( 'ReplyWithChanges' , 'ShowMessage' , ), 2070, (2070, (), [ (11, 49, 'True', None) , ], 1 , 1 , 4 , 0 , 348 , (3, 0, None, None) , 0 , )),
	(( 'EndReview' , ), 2071, (2071, (), [ ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'HasRevisionInfo' , 'HasRevisionInfo' , ), 2072, (2072, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 356 , (3, 0, None, None) , 0 , )),
	(( 'AddBaseline' , 'FileName' , ), 2073, (2073, (), [ (8, 49, "u''", None) , ], 1 , 1 , 4 , 0 , 360 , (3, 32, None, None) , 0 , )),
	(( 'RemoveBaseline' , ), 2074, (2074, (), [ ], 1 , 1 , 4 , 0 , 364 , (3, 0, None, None) , 0 , )),
	(( 'PasswordEncryptionProvider' , 'PasswordEncryptionProvider' , ), 2075, (2075, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'PasswordEncryptionAlgorithm' , 'PasswordEncryptionAlgorithm' , ), 2076, (2076, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 372 , (3, 0, None, None) , 0 , )),
	(( 'PasswordEncryptionKeyLength' , 'PasswordEncryptionKeyLength' , ), 2077, (2077, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'PasswordEncryptionFileProperties' , 'PasswordEncryptionFileProperties' , ), 2078, (2078, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 380 , (3, 0, None, None) , 0 , )),
	(( 'SetPasswordEncryptionOptions' , 'PasswordEncryptionProvider' , 'PasswordEncryptionAlgorithm' , 'PasswordEncryptionKeyLength' , 'PasswordEncryptionFileProperties' , 
			), 2079, (2079, (), [ (8, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Password' , 'Password' , ), 2080, (2080, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 388 , (3, 0, None, None) , 0 , )),
	(( 'Password' , 'Password' , ), 2080, (2080, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'WritePassword' , 'WritePassword' , ), 2081, (2081, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 396 , (3, 0, None, None) , 0 , )),
	(( 'WritePassword' , 'WritePassword' , ), 2081, (2081, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Permission' , 'Permission' , ), 2082, (2082, (), [ (16393, 10, None, "IID('{000C0376-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 404 , (3, 0, None, None) , 0 , )),
	(( 'SharedWorkspace' , 'SharedWorkspace' , ), 2083, (2083, (), [ (16393, 10, None, "IID('{000C0385-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Sync' , 'Sync' , ), 2084, (2084, (), [ (16393, 10, None, "IID('{000C0386-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 412 , (3, 0, None, None) , 0 , )),
	(( 'SendFaxOverInternet' , 'Recipients' , 'Subject' , 'ShowMessage' , ), 2085, (2085, (), [ 
			(8, 49, "u''", None) , (8, 49, "u''", None) , (11, 49, 'False', None) , ], 1 , 1 , 4 , 0 , 416 , (3, 32, None, None) , 0 , )),
	(( 'DocumentLibraryVersions' , 'DocumentLibraryVersions' , ), 2086, (2086, (), [ (16393, 10, None, "IID('{000C0388-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 420 , (3, 0, None, None) , 0 , )),
]

_Slide_vtables_dispatch_ = 1
_Slide_vtables_ = [
	(( 'Application' , 'Application' , ), 2001, (2001, (), [ (16397, 10, None, "IID('{91493441-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Parent' , ), 2002, (2002, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'Shapes' , 'Shapes' , ), 2003, (2003, (), [ (16393, 10, None, "IID('{91493475-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'HeadersFooters' , 'HeadersFooters' , ), 2004, (2004, (), [ (16393, 10, None, "IID('{91493474-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'SlideShowTransition' , 'SlideShowTransition' , ), 2005, (2005, (), [ (16393, 10, None, "IID('{91493471-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'ColorScheme' , 'ColorScheme' , ), 2006, (2006, (), [ (16393, 10, None, "IID('{9149346F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'ColorScheme' , 'ColorScheme' , ), 2006, (2006, (), [ (9, 1, None, "IID('{9149346F-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'Background' , 'Background' , ), 2007, (2007, (), [ (16393, 10, None, "IID('{9149347A-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 2008, (2008, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 2008, (2008, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SlideID' , 'SlideID' , ), 2009, (2009, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'PrintSteps' , 'PrintSteps' , ), 2010, (2010, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Select' , ), 2011, (2011, (), [ ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'Cut' , ), 2012, (2012, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Copy' , ), 2013, (2013, (), [ ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'Layout' , 'Layout' , ), 2014, (2014, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Layout' , 'Layout' , ), 2014, (2014, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'Duplicate' , 'Duplicate' , ), 2015, (2015, (), [ (16393, 10, None, "IID('{9149346B-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 2016, (2016, (), [ ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'Tags' , 'Tags' , ), 2017, (2017, (), [ (16393, 10, None, "IID('{914934B9-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SlideIndex' , 'SlideIndex' , ), 2018, (2018, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'SlideNumber' , 'SlideNumber' , ), 2019, (2019, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'DisplayMasterShapes' , 'DisplayMasterShapes' , ), 2020, (2020, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'DisplayMasterShapes' , 'DisplayMasterShapes' , ), 2020, (2020, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'FollowMasterBackground' , 'FollowMasterBackground' , ), 2021, (2021, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'FollowMasterBackground' , 'FollowMasterBackground' , ), 2021, (2021, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'NotesPage' , 'NotesPage' , ), 2022, (2022, (), [ (16393, 10, None, "IID('{9149346B-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'Master' , 'Master' , ), 2023, (2023, (), [ (16393, 10, None, "IID('{9149346C-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Hyperlinks' , 'Hyperlinks' , ), 2024, (2024, (), [ (16393, 10, None, "IID('{91493464-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'FileName' , 'FilterName' , 'ScaleWidth' , 'ScaleHeight' , 
			), 2025, (2025, (), [ (8, 1, None, None) , (8, 1, None, None) , (3, 49, '0', None) , (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Scripts' , 'Scripts' , ), 2026, (2026, (), [ (16393, 10, None, "IID('{000C0340-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( 'Comments' , 'Comments' , ), 2028, (2028, (), [ (16393, 10, None, "IID('{914934D4-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Design' , 'Design' , ), 2029, (2029, (), [ (16393, 10, None, "IID('{914934D7-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( 'Design' , 'Design' , ), 2029, (2029, (), [ (9, 1, None, "IID('{914934D7-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'MoveTo' , 'toPos' , ), 2030, (2030, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( 'TimeLine' , 'TimeLine' , ), 2031, (2031, (), [ (16393, 10, None, "IID('{914934DC-5A91-11CF-8700-00AA0060263B}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ApplyTemplate' , 'FileName' , ), 2032, (2032, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{914934E8-5A91-11CF-8700-00AA0060263B}' : RotationEffect,
	'{914934E9-5A91-11CF-8700-00AA0060263B}' : PropertyEffect,
	'{914934EA-5A91-11CF-8700-00AA0060263B}' : AnimationPoints,
	'{914934EB-5A91-11CF-8700-00AA0060263B}' : AnimationPoint,
	'{914934EC-5A91-11CF-8700-00AA0060263B}' : CanvasShapes,
	'{914934ED-5A91-11CF-8700-00AA0060263B}' : AutoCorrect,
	'{914934EE-5A91-11CF-8700-00AA0060263B}' : Options,
	'{914934EF-5A91-11CF-8700-00AA0060263B}' : CommandEffect,
	'{914934F0-5A91-11CF-8700-00AA0060263B}' : FilterEffect,
	'{914934F1-5A91-11CF-8700-00AA0060263B}' : SetEffect,
	'{91493441-5A91-11CF-8700-00AA0060263B}' : Application,
	'{91493442-5A91-11CF-8700-00AA0060263B}' : _Application,
	'{91493443-5A91-11CF-8700-00AA0060263B}' : Global,
	'{91493444-5A91-11CF-8700-00AA0060263B}' : Presentation,
	'{91493445-5A91-11CF-8700-00AA0060263B}' : Slide,
	'{91493446-5A91-11CF-8700-00AA0060263B}' : OLEControl,
	'{91493447-5A91-11CF-8700-00AA0060263B}' : Master,
	'{91493448-5A91-11CF-8700-00AA0060263B}' : PowerRex,
	'{91493450-5A91-11CF-8700-00AA0060263B}' : Collection,
	'{91493451-5A91-11CF-8700-00AA0060263B}' : _Global,
	'{91493452-5A91-11CF-8700-00AA0060263B}' : ColorFormat,
	'{91493453-5A91-11CF-8700-00AA0060263B}' : SlideShowWindow,
	'{91493454-5A91-11CF-8700-00AA0060263B}' : Selection,
	'{91493455-5A91-11CF-8700-00AA0060263B}' : DocumentWindows,
	'{91493456-5A91-11CF-8700-00AA0060263B}' : SlideShowWindows,
	'{91493457-5A91-11CF-8700-00AA0060263B}' : DocumentWindow,
	'{91493458-5A91-11CF-8700-00AA0060263B}' : View,
	'{91493459-5A91-11CF-8700-00AA0060263B}' : SlideShowView,
	'{9149345A-5A91-11CF-8700-00AA0060263B}' : SlideShowSettings,
	'{9149345B-5A91-11CF-8700-00AA0060263B}' : NamedSlideShows,
	'{9149345C-5A91-11CF-8700-00AA0060263B}' : NamedSlideShow,
	'{9149345D-5A91-11CF-8700-00AA0060263B}' : PrintOptions,
	'{9149345E-5A91-11CF-8700-00AA0060263B}' : PrintRanges,
	'{9149345F-5A91-11CF-8700-00AA0060263B}' : PrintRange,
	'{91493460-5A91-11CF-8700-00AA0060263B}' : AddIns,
	'{91493461-5A91-11CF-8700-00AA0060263B}' : AddIn,
	'{91493462-5A91-11CF-8700-00AA0060263B}' : Presentations,
	'{91493464-5A91-11CF-8700-00AA0060263B}' : Hyperlinks,
	'{91493465-5A91-11CF-8700-00AA0060263B}' : Hyperlink,
	'{91493466-5A91-11CF-8700-00AA0060263B}' : PageSetup,
	'{91493467-5A91-11CF-8700-00AA0060263B}' : Fonts,
	'{91493468-5A91-11CF-8700-00AA0060263B}' : ExtraColors,
	'{91493469-5A91-11CF-8700-00AA0060263B}' : Slides,
	'{9149346A-5A91-11CF-8700-00AA0060263B}' : _Slide,
	'{9149346B-5A91-11CF-8700-00AA0060263B}' : SlideRange,
	'{9149346C-5A91-11CF-8700-00AA0060263B}' : _Master,
	'{9149346E-5A91-11CF-8700-00AA0060263B}' : ColorSchemes,
	'{9149346F-5A91-11CF-8700-00AA0060263B}' : ColorScheme,
	'{91493470-5A91-11CF-8700-00AA0060263B}' : RGBColor,
	'{91493471-5A91-11CF-8700-00AA0060263B}' : SlideShowTransition,
	'{91493472-5A91-11CF-8700-00AA0060263B}' : SoundEffect,
	'{91493473-5A91-11CF-8700-00AA0060263B}' : SoundFormat,
	'{91493474-5A91-11CF-8700-00AA0060263B}' : HeadersFooters,
	'{91493475-5A91-11CF-8700-00AA0060263B}' : Shapes,
	'{91493476-5A91-11CF-8700-00AA0060263B}' : Placeholders,
	'{91493477-5A91-11CF-8700-00AA0060263B}' : PlaceholderFormat,
	'{91493478-5A91-11CF-8700-00AA0060263B}' : FreeformBuilder,
	'{91493479-5A91-11CF-8700-00AA0060263B}' : Shape,
	'{9149347A-5A91-11CF-8700-00AA0060263B}' : ShapeRange,
	'{9149347B-5A91-11CF-8700-00AA0060263B}' : GroupShapes,
	'{9149347C-5A91-11CF-8700-00AA0060263B}' : Adjustments,
	'{9149347D-5A91-11CF-8700-00AA0060263B}' : PictureFormat,
	'{9149347E-5A91-11CF-8700-00AA0060263B}' : FillFormat,
	'{9149347F-5A91-11CF-8700-00AA0060263B}' : LineFormat,
	'{91493480-5A91-11CF-8700-00AA0060263B}' : ShadowFormat,
	'{91493481-5A91-11CF-8700-00AA0060263B}' : ConnectorFormat,
	'{91493482-5A91-11CF-8700-00AA0060263B}' : TextEffectFormat,
	'{91493483-5A91-11CF-8700-00AA0060263B}' : ThreeDFormat,
	'{91493484-5A91-11CF-8700-00AA0060263B}' : TextFrame,
	'{91493485-5A91-11CF-8700-00AA0060263B}' : CalloutFormat,
	'{91493486-5A91-11CF-8700-00AA0060263B}' : ShapeNodes,
	'{91493487-5A91-11CF-8700-00AA0060263B}' : ShapeNode,
	'{91493488-5A91-11CF-8700-00AA0060263B}' : OLEFormat,
	'{91493489-5A91-11CF-8700-00AA0060263B}' : LinkFormat,
	'{9149348A-5A91-11CF-8700-00AA0060263B}' : ObjectVerbs,
	'{9149348B-5A91-11CF-8700-00AA0060263B}' : AnimationSettings,
	'{9149348C-5A91-11CF-8700-00AA0060263B}' : ActionSettings,
	'{9149348D-5A91-11CF-8700-00AA0060263B}' : ActionSetting,
	'{9149348E-5A91-11CF-8700-00AA0060263B}' : PlaySettings,
	'{9149348F-5A91-11CF-8700-00AA0060263B}' : TextRange,
	'{91493490-5A91-11CF-8700-00AA0060263B}' : Ruler,
	'{91493491-5A91-11CF-8700-00AA0060263B}' : RulerLevels,
	'{91493492-5A91-11CF-8700-00AA0060263B}' : RulerLevel,
	'{91493493-5A91-11CF-8700-00AA0060263B}' : TabStops,
	'{91493494-5A91-11CF-8700-00AA0060263B}' : TabStop,
	'{91493495-5A91-11CF-8700-00AA0060263B}' : Font,
	'{91493496-5A91-11CF-8700-00AA0060263B}' : ParagraphFormat,
	'{91493497-5A91-11CF-8700-00AA0060263B}' : BulletFormat,
	'{91493498-5A91-11CF-8700-00AA0060263B}' : TextStyles,
	'{91493499-5A91-11CF-8700-00AA0060263B}' : TextStyle,
	'{9149349A-5A91-11CF-8700-00AA0060263B}' : TextStyleLevels,
	'{9149349B-5A91-11CF-8700-00AA0060263B}' : TextStyleLevel,
	'{9149349C-5A91-11CF-8700-00AA0060263B}' : HeaderFooter,
	'{9149349D-5A91-11CF-8700-00AA0060263B}' : _Presentation,
	'{914934B9-5A91-11CF-8700-00AA0060263B}' : Tags,
	'{914934C0-5A91-11CF-8700-00AA0060263B}' : OCXExtender,
	'{914934C1-5A91-11CF-8700-00AA0060263B}' : OCXExtenderEvents,
	'{914934C2-5A91-11CF-8700-00AA0060263B}' : EApplication,
	'{914934C3-5A91-11CF-8700-00AA0060263B}' : Table,
	'{914934C4-5A91-11CF-8700-00AA0060263B}' : Columns,
	'{914934C5-5A91-11CF-8700-00AA0060263B}' : Column,
	'{914934C6-5A91-11CF-8700-00AA0060263B}' : Rows,
	'{914934C7-5A91-11CF-8700-00AA0060263B}' : Row,
	'{914934C8-5A91-11CF-8700-00AA0060263B}' : CellRange,
	'{914934C9-5A91-11CF-8700-00AA0060263B}' : Cell,
	'{914934CA-5A91-11CF-8700-00AA0060263B}' : Borders,
	'{914934CB-5A91-11CF-8700-00AA0060263B}' : Panes,
	'{914934CC-5A91-11CF-8700-00AA0060263B}' : Pane,
	'{914934CD-5A91-11CF-8700-00AA0060263B}' : DefaultWebOptions,
	'{914934CE-5A91-11CF-8700-00AA0060263B}' : WebOptions,
	'{914934CF-5A91-11CF-8700-00AA0060263B}' : PublishObjects,
	'{914934D0-5A91-11CF-8700-00AA0060263B}' : PublishObject,
	'{914934D3-5A91-11CF-8700-00AA0060263B}' : _PowerRex,
	'{914934D4-5A91-11CF-8700-00AA0060263B}' : Comments,
	'{914934D5-5A91-11CF-8700-00AA0060263B}' : Comment,
	'{914934D6-5A91-11CF-8700-00AA0060263B}' : Designs,
	'{914934D7-5A91-11CF-8700-00AA0060263B}' : Design,
	'{914934D8-5A91-11CF-8700-00AA0060263B}' : DiagramNode,
	'{914934D9-5A91-11CF-8700-00AA0060263B}' : DiagramNodeChildren,
	'{914934DA-5A91-11CF-8700-00AA0060263B}' : DiagramNodes,
	'{914934DB-5A91-11CF-8700-00AA0060263B}' : Diagram,
	'{914934DC-5A91-11CF-8700-00AA0060263B}' : TimeLine,
	'{914934DD-5A91-11CF-8700-00AA0060263B}' : Sequences,
	'{914934DE-5A91-11CF-8700-00AA0060263B}' : Sequence,
	'{914934DF-5A91-11CF-8700-00AA0060263B}' : Effect,
	'{914934E0-5A91-11CF-8700-00AA0060263B}' : Timing,
	'{914934E1-5A91-11CF-8700-00AA0060263B}' : EffectParameters,
	'{914934E2-5A91-11CF-8700-00AA0060263B}' : EffectInformation,
	'{914934E3-5A91-11CF-8700-00AA0060263B}' : AnimationBehaviors,
	'{914934E4-5A91-11CF-8700-00AA0060263B}' : AnimationBehavior,
	'{914934E5-5A91-11CF-8700-00AA0060263B}' : MotionEffect,
	'{914934E6-5A91-11CF-8700-00AA0060263B}' : ColorEffect,
	'{914934E7-5A91-11CF-8700-00AA0060263B}' : ScaleEffect,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{914934E8-5A91-11CF-8700-00AA0060263B}' : 'RotationEffect',
	'{914934E9-5A91-11CF-8700-00AA0060263B}' : 'PropertyEffect',
	'{914934EA-5A91-11CF-8700-00AA0060263B}' : 'AnimationPoints',
	'{914934EB-5A91-11CF-8700-00AA0060263B}' : 'AnimationPoint',
	'{914934EC-5A91-11CF-8700-00AA0060263B}' : 'CanvasShapes',
	'{914934ED-5A91-11CF-8700-00AA0060263B}' : 'AutoCorrect',
	'{914934EE-5A91-11CF-8700-00AA0060263B}' : 'Options',
	'{914934EF-5A91-11CF-8700-00AA0060263B}' : 'CommandEffect',
	'{914934F0-5A91-11CF-8700-00AA0060263B}' : 'FilterEffect',
	'{914934F1-5A91-11CF-8700-00AA0060263B}' : 'SetEffect',
	'{91493442-5A91-11CF-8700-00AA0060263B}' : '_Application',
	'{91493450-5A91-11CF-8700-00AA0060263B}' : 'Collection',
	'{91493451-5A91-11CF-8700-00AA0060263B}' : '_Global',
	'{91493452-5A91-11CF-8700-00AA0060263B}' : 'ColorFormat',
	'{91493453-5A91-11CF-8700-00AA0060263B}' : 'SlideShowWindow',
	'{91493454-5A91-11CF-8700-00AA0060263B}' : 'Selection',
	'{91493455-5A91-11CF-8700-00AA0060263B}' : 'DocumentWindows',
	'{91493456-5A91-11CF-8700-00AA0060263B}' : 'SlideShowWindows',
	'{91493457-5A91-11CF-8700-00AA0060263B}' : 'DocumentWindow',
	'{91493458-5A91-11CF-8700-00AA0060263B}' : 'View',
	'{91493459-5A91-11CF-8700-00AA0060263B}' : 'SlideShowView',
	'{9149345A-5A91-11CF-8700-00AA0060263B}' : 'SlideShowSettings',
	'{9149345B-5A91-11CF-8700-00AA0060263B}' : 'NamedSlideShows',
	'{9149345C-5A91-11CF-8700-00AA0060263B}' : 'NamedSlideShow',
	'{9149345D-5A91-11CF-8700-00AA0060263B}' : 'PrintOptions',
	'{9149345E-5A91-11CF-8700-00AA0060263B}' : 'PrintRanges',
	'{9149345F-5A91-11CF-8700-00AA0060263B}' : 'PrintRange',
	'{91493460-5A91-11CF-8700-00AA0060263B}' : 'AddIns',
	'{91493461-5A91-11CF-8700-00AA0060263B}' : 'AddIn',
	'{91493462-5A91-11CF-8700-00AA0060263B}' : 'Presentations',
	'{91493463-5A91-11CF-8700-00AA0060263B}' : 'PresEvents',
	'{91493464-5A91-11CF-8700-00AA0060263B}' : 'Hyperlinks',
	'{91493465-5A91-11CF-8700-00AA0060263B}' : 'Hyperlink',
	'{91493466-5A91-11CF-8700-00AA0060263B}' : 'PageSetup',
	'{91493467-5A91-11CF-8700-00AA0060263B}' : 'Fonts',
	'{91493468-5A91-11CF-8700-00AA0060263B}' : 'ExtraColors',
	'{91493469-5A91-11CF-8700-00AA0060263B}' : 'Slides',
	'{9149346A-5A91-11CF-8700-00AA0060263B}' : '_Slide',
	'{9149346B-5A91-11CF-8700-00AA0060263B}' : 'SlideRange',
	'{9149346C-5A91-11CF-8700-00AA0060263B}' : '_Master',
	'{9149346D-5A91-11CF-8700-00AA0060263B}' : 'SldEvents',
	'{9149346E-5A91-11CF-8700-00AA0060263B}' : 'ColorSchemes',
	'{9149346F-5A91-11CF-8700-00AA0060263B}' : 'ColorScheme',
	'{91493470-5A91-11CF-8700-00AA0060263B}' : 'RGBColor',
	'{91493471-5A91-11CF-8700-00AA0060263B}' : 'SlideShowTransition',
	'{91493472-5A91-11CF-8700-00AA0060263B}' : 'SoundEffect',
	'{91493473-5A91-11CF-8700-00AA0060263B}' : 'SoundFormat',
	'{91493474-5A91-11CF-8700-00AA0060263B}' : 'HeadersFooters',
	'{91493475-5A91-11CF-8700-00AA0060263B}' : 'Shapes',
	'{91493476-5A91-11CF-8700-00AA0060263B}' : 'Placeholders',
	'{91493477-5A91-11CF-8700-00AA0060263B}' : 'PlaceholderFormat',
	'{91493478-5A91-11CF-8700-00AA0060263B}' : 'FreeformBuilder',
	'{91493479-5A91-11CF-8700-00AA0060263B}' : 'Shape',
	'{9149347A-5A91-11CF-8700-00AA0060263B}' : 'ShapeRange',
	'{9149347B-5A91-11CF-8700-00AA0060263B}' : 'GroupShapes',
	'{9149347C-5A91-11CF-8700-00AA0060263B}' : 'Adjustments',
	'{9149347D-5A91-11CF-8700-00AA0060263B}' : 'PictureFormat',
	'{9149347E-5A91-11CF-8700-00AA0060263B}' : 'FillFormat',
	'{9149347F-5A91-11CF-8700-00AA0060263B}' : 'LineFormat',
	'{91493480-5A91-11CF-8700-00AA0060263B}' : 'ShadowFormat',
	'{91493481-5A91-11CF-8700-00AA0060263B}' : 'ConnectorFormat',
	'{91493482-5A91-11CF-8700-00AA0060263B}' : 'TextEffectFormat',
	'{91493483-5A91-11CF-8700-00AA0060263B}' : 'ThreeDFormat',
	'{91493484-5A91-11CF-8700-00AA0060263B}' : 'TextFrame',
	'{91493485-5A91-11CF-8700-00AA0060263B}' : 'CalloutFormat',
	'{91493486-5A91-11CF-8700-00AA0060263B}' : 'ShapeNodes',
	'{91493487-5A91-11CF-8700-00AA0060263B}' : 'ShapeNode',
	'{91493488-5A91-11CF-8700-00AA0060263B}' : 'OLEFormat',
	'{91493489-5A91-11CF-8700-00AA0060263B}' : 'LinkFormat',
	'{9149348A-5A91-11CF-8700-00AA0060263B}' : 'ObjectVerbs',
	'{9149348B-5A91-11CF-8700-00AA0060263B}' : 'AnimationSettings',
	'{9149348C-5A91-11CF-8700-00AA0060263B}' : 'ActionSettings',
	'{9149348D-5A91-11CF-8700-00AA0060263B}' : 'ActionSetting',
	'{9149348E-5A91-11CF-8700-00AA0060263B}' : 'PlaySettings',
	'{9149348F-5A91-11CF-8700-00AA0060263B}' : 'TextRange',
	'{91493490-5A91-11CF-8700-00AA0060263B}' : 'Ruler',
	'{91493491-5A91-11CF-8700-00AA0060263B}' : 'RulerLevels',
	'{91493492-5A91-11CF-8700-00AA0060263B}' : 'RulerLevel',
	'{91493493-5A91-11CF-8700-00AA0060263B}' : 'TabStops',
	'{91493494-5A91-11CF-8700-00AA0060263B}' : 'TabStop',
	'{91493495-5A91-11CF-8700-00AA0060263B}' : 'Font',
	'{91493496-5A91-11CF-8700-00AA0060263B}' : 'ParagraphFormat',
	'{91493497-5A91-11CF-8700-00AA0060263B}' : 'BulletFormat',
	'{91493498-5A91-11CF-8700-00AA0060263B}' : 'TextStyles',
	'{91493499-5A91-11CF-8700-00AA0060263B}' : 'TextStyle',
	'{9149349A-5A91-11CF-8700-00AA0060263B}' : 'TextStyleLevels',
	'{9149349B-5A91-11CF-8700-00AA0060263B}' : 'TextStyleLevel',
	'{9149349C-5A91-11CF-8700-00AA0060263B}' : 'HeaderFooter',
	'{9149349D-5A91-11CF-8700-00AA0060263B}' : '_Presentation',
	'{914934B9-5A91-11CF-8700-00AA0060263B}' : 'Tags',
	'{914934BE-5A91-11CF-8700-00AA0060263B}' : 'MouseTracker',
	'{914934BF-5A91-11CF-8700-00AA0060263B}' : 'MouseDownHandler',
	'{914934C0-5A91-11CF-8700-00AA0060263B}' : 'OCXExtender',
	'{914934C3-5A91-11CF-8700-00AA0060263B}' : 'Table',
	'{914934C4-5A91-11CF-8700-00AA0060263B}' : 'Columns',
	'{914934C5-5A91-11CF-8700-00AA0060263B}' : 'Column',
	'{914934C6-5A91-11CF-8700-00AA0060263B}' : 'Rows',
	'{914934C7-5A91-11CF-8700-00AA0060263B}' : 'Row',
	'{914934C8-5A91-11CF-8700-00AA0060263B}' : 'CellRange',
	'{914934C9-5A91-11CF-8700-00AA0060263B}' : 'Cell',
	'{914934CA-5A91-11CF-8700-00AA0060263B}' : 'Borders',
	'{914934CB-5A91-11CF-8700-00AA0060263B}' : 'Panes',
	'{914934CC-5A91-11CF-8700-00AA0060263B}' : 'Pane',
	'{914934CD-5A91-11CF-8700-00AA0060263B}' : 'DefaultWebOptions',
	'{914934CE-5A91-11CF-8700-00AA0060263B}' : 'WebOptions',
	'{914934CF-5A91-11CF-8700-00AA0060263B}' : 'PublishObjects',
	'{914934D0-5A91-11CF-8700-00AA0060263B}' : 'PublishObject',
	'{914934D2-5A91-11CF-8700-00AA0060263B}' : 'MasterEvents',
	'{914934D3-5A91-11CF-8700-00AA0060263B}' : '_PowerRex',
	'{914934D4-5A91-11CF-8700-00AA0060263B}' : 'Comments',
	'{914934D5-5A91-11CF-8700-00AA0060263B}' : 'Comment',
	'{914934D6-5A91-11CF-8700-00AA0060263B}' : 'Designs',
	'{914934D7-5A91-11CF-8700-00AA0060263B}' : 'Design',
	'{914934D8-5A91-11CF-8700-00AA0060263B}' : 'DiagramNode',
	'{914934D9-5A91-11CF-8700-00AA0060263B}' : 'DiagramNodeChildren',
	'{914934DA-5A91-11CF-8700-00AA0060263B}' : 'DiagramNodes',
	'{914934DB-5A91-11CF-8700-00AA0060263B}' : 'Diagram',
	'{914934DC-5A91-11CF-8700-00AA0060263B}' : 'TimeLine',
	'{914934DD-5A91-11CF-8700-00AA0060263B}' : 'Sequences',
	'{914934DE-5A91-11CF-8700-00AA0060263B}' : 'Sequence',
	'{914934DF-5A91-11CF-8700-00AA0060263B}' : 'Effect',
	'{914934E0-5A91-11CF-8700-00AA0060263B}' : 'Timing',
	'{914934E1-5A91-11CF-8700-00AA0060263B}' : 'EffectParameters',
	'{914934E2-5A91-11CF-8700-00AA0060263B}' : 'EffectInformation',
	'{914934E3-5A91-11CF-8700-00AA0060263B}' : 'AnimationBehaviors',
	'{914934E4-5A91-11CF-8700-00AA0060263B}' : 'AnimationBehavior',
	'{914934E5-5A91-11CF-8700-00AA0060263B}' : 'MotionEffect',
	'{914934E6-5A91-11CF-8700-00AA0060263B}' : 'ColorEffect',
	'{914934E7-5A91-11CF-8700-00AA0060263B}' : 'ScaleEffect',
}


NamesToIIDMap = {
	'CanvasShapes' : '{914934EC-5A91-11CF-8700-00AA0060263B}',
	'RulerLevel' : '{91493492-5A91-11CF-8700-00AA0060263B}',
	'MasterEvents' : '{914934D2-5A91-11CF-8700-00AA0060263B}',
	'ThreeDFormat' : '{91493483-5A91-11CF-8700-00AA0060263B}',
	'PresEvents' : '{91493463-5A91-11CF-8700-00AA0060263B}',
	'ColorScheme' : '{9149346F-5A91-11CF-8700-00AA0060263B}',
	'Ruler' : '{91493490-5A91-11CF-8700-00AA0060263B}',
	'ObjectVerbs' : '{9149348A-5A91-11CF-8700-00AA0060263B}',
	'ActionSettings' : '{9149348C-5A91-11CF-8700-00AA0060263B}',
	'TabStops' : '{91493493-5A91-11CF-8700-00AA0060263B}',
	'AddIn' : '{91493461-5A91-11CF-8700-00AA0060263B}',
	'DefaultWebOptions' : '{914934CD-5A91-11CF-8700-00AA0060263B}',
	'PublishObject' : '{914934D0-5A91-11CF-8700-00AA0060263B}',
	'CalloutFormat' : '{91493485-5A91-11CF-8700-00AA0060263B}',
	'Comments' : '{914934D4-5A91-11CF-8700-00AA0060263B}',
	'PictureFormat' : '{9149347D-5A91-11CF-8700-00AA0060263B}',
	'MouseDownHandler' : '{914934BF-5A91-11CF-8700-00AA0060263B}',
	'_PowerRex' : '{914934D3-5A91-11CF-8700-00AA0060263B}',
	'ShapeNodes' : '{91493486-5A91-11CF-8700-00AA0060263B}',
	'_Global' : '{91493451-5A91-11CF-8700-00AA0060263B}',
	'Pane' : '{914934CC-5A91-11CF-8700-00AA0060263B}',
	'MotionEffect' : '{914934E5-5A91-11CF-8700-00AA0060263B}',
	'Font' : '{91493495-5A91-11CF-8700-00AA0060263B}',
	'TextStyle' : '{91493499-5A91-11CF-8700-00AA0060263B}',
	'_Application' : '{91493442-5A91-11CF-8700-00AA0060263B}',
	'Hyperlinks' : '{91493464-5A91-11CF-8700-00AA0060263B}',
	'Placeholders' : '{91493476-5A91-11CF-8700-00AA0060263B}',
	'_Slide' : '{9149346A-5A91-11CF-8700-00AA0060263B}',
	'AnimationPoint' : '{914934EB-5A91-11CF-8700-00AA0060263B}',
	'WebOptions' : '{914934CE-5A91-11CF-8700-00AA0060263B}',
	'LinkFormat' : '{91493489-5A91-11CF-8700-00AA0060263B}',
	'EffectParameters' : '{914934E1-5A91-11CF-8700-00AA0060263B}',
	'ShapeRange' : '{9149347A-5A91-11CF-8700-00AA0060263B}',
	'ColorEffect' : '{914934E6-5A91-11CF-8700-00AA0060263B}',
	'FillFormat' : '{9149347E-5A91-11CF-8700-00AA0060263B}',
	'AddIns' : '{91493460-5A91-11CF-8700-00AA0060263B}',
	'NamedSlideShows' : '{9149345B-5A91-11CF-8700-00AA0060263B}',
	'PrintRanges' : '{9149345E-5A91-11CF-8700-00AA0060263B}',
	'PublishObjects' : '{914934CF-5A91-11CF-8700-00AA0060263B}',
	'ShadowFormat' : '{91493480-5A91-11CF-8700-00AA0060263B}',
	'TimeLine' : '{914934DC-5A91-11CF-8700-00AA0060263B}',
	'DocumentWindow' : '{91493457-5A91-11CF-8700-00AA0060263B}',
	'Presentations' : '{91493462-5A91-11CF-8700-00AA0060263B}',
	'Shapes' : '{91493475-5A91-11CF-8700-00AA0060263B}',
	'PlaySettings' : '{9149348E-5A91-11CF-8700-00AA0060263B}',
	'OLEFormat' : '{91493488-5A91-11CF-8700-00AA0060263B}',
	'SoundEffect' : '{91493472-5A91-11CF-8700-00AA0060263B}',
	'NamedSlideShow' : '{9149345C-5A91-11CF-8700-00AA0060263B}',
	'AnimationSettings' : '{9149348B-5A91-11CF-8700-00AA0060263B}',
	'FreeformBuilder' : '{91493478-5A91-11CF-8700-00AA0060263B}',
	'Options' : '{914934EE-5A91-11CF-8700-00AA0060263B}',
	'Comment' : '{914934D5-5A91-11CF-8700-00AA0060263B}',
	'Selection' : '{91493454-5A91-11CF-8700-00AA0060263B}',
	'Tags' : '{914934B9-5A91-11CF-8700-00AA0060263B}',
	'BulletFormat' : '{91493497-5A91-11CF-8700-00AA0060263B}',
	'EApplication' : '{914934C2-5A91-11CF-8700-00AA0060263B}',
	'Shape' : '{91493479-5A91-11CF-8700-00AA0060263B}',
	'Design' : '{914934D7-5A91-11CF-8700-00AA0060263B}',
	'LineFormat' : '{9149347F-5A91-11CF-8700-00AA0060263B}',
	'Row' : '{914934C7-5A91-11CF-8700-00AA0060263B}',
	'SlideShowSettings' : '{9149345A-5A91-11CF-8700-00AA0060263B}',
	'PrintOptions' : '{9149345D-5A91-11CF-8700-00AA0060263B}',
	'PrintRange' : '{9149345F-5A91-11CF-8700-00AA0060263B}',
	'Effect' : '{914934DF-5A91-11CF-8700-00AA0060263B}',
	'Cell' : '{914934C9-5A91-11CF-8700-00AA0060263B}',
	'HeadersFooters' : '{91493474-5A91-11CF-8700-00AA0060263B}',
	'CellRange' : '{914934C8-5A91-11CF-8700-00AA0060263B}',
	'SlideShowWindows' : '{91493456-5A91-11CF-8700-00AA0060263B}',
	'TextStyleLevel' : '{9149349B-5A91-11CF-8700-00AA0060263B}',
	'Collection' : '{91493450-5A91-11CF-8700-00AA0060263B}',
	'Borders' : '{914934CA-5A91-11CF-8700-00AA0060263B}',
	'ColorFormat' : '{91493452-5A91-11CF-8700-00AA0060263B}',
	'TextRange' : '{9149348F-5A91-11CF-8700-00AA0060263B}',
	'Columns' : '{914934C4-5A91-11CF-8700-00AA0060263B}',
	'ExtraColors' : '{91493468-5A91-11CF-8700-00AA0060263B}',
	'Designs' : '{914934D6-5A91-11CF-8700-00AA0060263B}',
	'DiagramNode' : '{914934D8-5A91-11CF-8700-00AA0060263B}',
	'RotationEffect' : '{914934E8-5A91-11CF-8700-00AA0060263B}',
	'AnimationBehavior' : '{914934E4-5A91-11CF-8700-00AA0060263B}',
	'CommandEffect' : '{914934EF-5A91-11CF-8700-00AA0060263B}',
	'PropertyEffect' : '{914934E9-5A91-11CF-8700-00AA0060263B}',
	'ParagraphFormat' : '{91493496-5A91-11CF-8700-00AA0060263B}',
	'DiagramNodes' : '{914934DA-5A91-11CF-8700-00AA0060263B}',
	'ConnectorFormat' : '{91493481-5A91-11CF-8700-00AA0060263B}',
	'EffectInformation' : '{914934E2-5A91-11CF-8700-00AA0060263B}',
	'HeaderFooter' : '{9149349C-5A91-11CF-8700-00AA0060263B}',
	'SlideShowWindow' : '{91493453-5A91-11CF-8700-00AA0060263B}',
	'SetEffect' : '{914934F1-5A91-11CF-8700-00AA0060263B}',
	'_Presentation' : '{9149349D-5A91-11CF-8700-00AA0060263B}',
	'Column' : '{914934C5-5A91-11CF-8700-00AA0060263B}',
	'Fonts' : '{91493467-5A91-11CF-8700-00AA0060263B}',
	'SlideRange' : '{9149346B-5A91-11CF-8700-00AA0060263B}',
	'DiagramNodeChildren' : '{914934D9-5A91-11CF-8700-00AA0060263B}',
	'ActionSetting' : '{9149348D-5A91-11CF-8700-00AA0060263B}',
	'OCXExtender' : '{914934C0-5A91-11CF-8700-00AA0060263B}',
	'ShapeNode' : '{91493487-5A91-11CF-8700-00AA0060263B}',
	'RGBColor' : '{91493470-5A91-11CF-8700-00AA0060263B}',
	'DocumentWindows' : '{91493455-5A91-11CF-8700-00AA0060263B}',
	'PlaceholderFormat' : '{91493477-5A91-11CF-8700-00AA0060263B}',
	'FilterEffect' : '{914934F0-5A91-11CF-8700-00AA0060263B}',
	'SldEvents' : '{9149346D-5A91-11CF-8700-00AA0060263B}',
	'Rows' : '{914934C6-5A91-11CF-8700-00AA0060263B}',
	'ScaleEffect' : '{914934E7-5A91-11CF-8700-00AA0060263B}',
	'TextFrame' : '{91493484-5A91-11CF-8700-00AA0060263B}',
	'Panes' : '{914934CB-5A91-11CF-8700-00AA0060263B}',
	'RulerLevels' : '{91493491-5A91-11CF-8700-00AA0060263B}',
	'MouseTracker' : '{914934BE-5A91-11CF-8700-00AA0060263B}',
	'OCXExtenderEvents' : '{914934C1-5A91-11CF-8700-00AA0060263B}',
	'TabStop' : '{91493494-5A91-11CF-8700-00AA0060263B}',
	'Slides' : '{91493469-5A91-11CF-8700-00AA0060263B}',
	'TextStyleLevels' : '{9149349A-5A91-11CF-8700-00AA0060263B}',
	'Timing' : '{914934E0-5A91-11CF-8700-00AA0060263B}',
	'SoundFormat' : '{91493473-5A91-11CF-8700-00AA0060263B}',
	'Hyperlink' : '{91493465-5A91-11CF-8700-00AA0060263B}',
	'AnimationBehaviors' : '{914934E3-5A91-11CF-8700-00AA0060263B}',
	'SlideShowView' : '{91493459-5A91-11CF-8700-00AA0060263B}',
	'TextEffectFormat' : '{91493482-5A91-11CF-8700-00AA0060263B}',
	'AnimationPoints' : '{914934EA-5A91-11CF-8700-00AA0060263B}',
	'_Master' : '{9149346C-5A91-11CF-8700-00AA0060263B}',
	'View' : '{91493458-5A91-11CF-8700-00AA0060263B}',
	'TextStyles' : '{91493498-5A91-11CF-8700-00AA0060263B}',
	'Diagram' : '{914934DB-5A91-11CF-8700-00AA0060263B}',
	'Sequence' : '{914934DE-5A91-11CF-8700-00AA0060263B}',
	'AutoCorrect' : '{914934ED-5A91-11CF-8700-00AA0060263B}',
	'Adjustments' : '{9149347C-5A91-11CF-8700-00AA0060263B}',
	'SlideShowTransition' : '{91493471-5A91-11CF-8700-00AA0060263B}',
	'GroupShapes' : '{9149347B-5A91-11CF-8700-00AA0060263B}',
	'Sequences' : '{914934DD-5A91-11CF-8700-00AA0060263B}',
	'Table' : '{914934C3-5A91-11CF-8700-00AA0060263B}',
	'ColorSchemes' : '{9149346E-5A91-11CF-8700-00AA0060263B}',
	'PageSetup' : '{91493466-5A91-11CF-8700-00AA0060263B}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

