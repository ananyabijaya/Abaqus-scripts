# Creating constraints
import numpy as np


def create_pbc_constraints(fronts, backs, tops, bots):
    """ Function to create periodic boundary conditions for a
	heterogeneous RVE by creating constraint equation between periodic
	nodes in ABAQUS.
	Args:
		fronts (List): List of nodes on the front boundary
		backs (List):  List of nodes corresponding to front boundary nodes
		tops (List):   List of nodes on the top boundary
		bots (List):   List of nodes corresponding to top boundary nodes
		c2   (Abaqus Node): Top-left node
		c5   (Abaqus Node): Bottom-Right node
		c6   (Abaqus Node): Bottom-Left node
	Returns:
		None
	"""
    modelName = "Model-1"
    for i in mdb.models[modelName].constraints.keys():
        del mdb.models[modelName].constraints[i]
        print(i)
    print(tops)
    n = 0
    for i, k in zip(tops, bots):
        n = n + 1
        mdb.models[modelName].Equation(
            name="X_tops-bots%s" % i,
            terms=(
                (1.0, "tops%s" % i, 1),
                (-1.0, "bots%s" % k, 1),
                (1.0, "c6", 1),
                (-1.0, "c2", 1),
            ),
        )
    print(n)
    for i, k in zip(fronts, backs):
        n = n + 1
        mdb.models[modelName].Equation(
            name="X_fronts-backs%s" % i,
            terms=(
                (1.0, "fronts%s" % i, 1),
                (-1.0, "backs%s" % k, 1),
                (1.0, "c6", 1),
                (-1.0, "c5", 1),
            ),
        )
    print(n)
    for i, k in zip(tops, bots):
        n = n + 1
        mdb.models[modelName].Equation(
            name="Y_tops-bots%s" % i,
            terms=(
                (1.0, "tops%s" % i, 2),
                (-1.0, "bots%s" % k, 2),
                (1.0, "c6", 2),
                (-1.0, "c2", 2),
            ),
        )
    print(n)
    for i, k in zip(fronts, backs):
        n = n + 1
        mdb.models[modelName].Equation(
            name="Y_fronts-backs%s" % i,
            terms=(
                (1.0, "fronts%s" % i, 2),
                (-1.0, "backs%s" % k, 2),
                (1.0, "c6", 2),
                (-1.0, "c5", 2),
            ),
        )
    print(n)
    return


def create_pbc_constraints_lattice(fronts, backs, tops, bots):
    """ Function to create periodic boundary conditions for a
	lattice RVE by creating constraint equation between periodic
	nodes in ABAQUS.

	Args:
		fronts (List): List of nodes on the front boundary 
		backs (List):  List of nodes corresponding to front boundary nodes
		tops (List):   List of nodes on the top boundary 
		bots (List):   List of nodes corresponding to top boundary nodes
		p1   (Abaqus Node):  Bottom most node on the back (left) boundary
		p2   (Abaqus Node):  Bottom most node on the front (right) boundary
		p3   (Abaqus Node):  Left most node on the bottom boundary	
		p4   (Abaqus Node):  Left most node on the top boundary 

	Returns:
		None
	"""
    modelName = "Model-1"
    for i in mdb.models[modelName].constraints.keys():
        del mdb.models[modelName].constraints[i]
        print(i)
    print(tops)
    n = 0
    for i, k in zip(tops, bots):
        n = n + 1
        mdb.models[modelName].Equation(
            name="X_tops-bots%s" % i,
            terms=(
                (1.0, "tops%s" % i, 1),
                (-1.0, "bots%s" % k, 1),
                (1.0, "p3", 1),
                (-1.0, "p4", 1),
            ),
        )
    print(n)
    for i, k in zip(fronts, backs):
        n = n + 1
        mdb.models[modelName].Equation(
            name="X_fronts-backs%s" % i,
            terms=(
                (1.0, "fronts%s" % i, 1),
                (-1.0, "backs%s" % k, 1),
                (1.0, "p1", 1),
                (-1.0, "p2", 1),
            ),
        )
    print(n)
    for i, k in zip(tops, bots):
        n = n + 1
        mdb.models[modelName].Equation(
            name="Y_tops-bots%s" % i,
            terms=(
                (1.0, "tops%s" % i, 2),
                (-1.0, "bots%s" % k, 2),
                (1.0, "p3", 2),
                (-1.0, "p4", 2),
            ),
        )
    print(n)
    for i, k in zip(fronts, backs):
        n = n + 1
        mdb.models[modelName].Equation(
            name="Y_fronts-backs%s" % i,
            terms=(
                (1.0, "fronts%s" % i, 2),
                (-1.0, "backs%s" % k, 2),
                (1.0, "p1", 2),
                (-1.0, "p2", 2),
            ),
        )
    print(n)
    return
   

backs = [11620,3292,11619,3291,11618,3290,11617,3289,11616,11615,3288,11614,3287,11613,3286,11612,3285,11611,3284,11610,3283,11609,3282,11608,3281,11607,3280,11606,3279,11605,11604,3278,11603,3277,11602,3276,11601,3275,11600,3274,11599,3273,11598,3272,11597,3271,11596,3270,11595,11594,3269,11593,3268,11592,3267,11591,3266,11590,3265,11589,3264,11588,3263,11587,3262,11586,3261,11585,3260,11584,11583,3259,11582,3258,11581,3257,11580,3256,11579,3255,11578,3254,11577,3253,11576,3252,11575,3251,11574,11573,3250,11572,3249,11571,3248,11570,3247,11569,3246,11568,3245,11567,3244,11566,3243,11565,3242,11564,3241,11563,11562,3240,11561,3239,11560,3238,11559,3237,11558,3236,11557,3235,11556,3234,11555,3233,11554,3232,11553,11552,3231,11551,3230,11550,3229,11549,3228,11548,3227,11547,3226,11546,3225,11545,3224,11544,3223,11543,3222,11542,11541,3221,11540,3220,11539,3219,11538,3218,11537,3217,11495,3180,11496,3181,11497,3182,11498,3183,11499,11500,3184,11501,3185,11502,3186,11503,3187,11504,3188,11505,3189,11506,3190,11507,3191,11508,3192,11509,3193,11510,11511,3194,11512,3195,11513,3196,11514,3197,11515,3198,11516,3199,11517,3200,11518,3201,11519,3202,11520,11521,3203,11522,3204,11523,3205,11524,3206,11525,3207,11526,3208,11527,3209,11528,3210,11529,3211,11530,3212,11531,11532,3213,11533,3214,11534,3215,11535,3216,11536]
fronts = [11124,2919,11125,2920,11126,2921,11127,2922,11128,11129,2923,11130,2924,11131,2925,11132,2926,11133,2927,11134,2928,11135,2929,11136,2930,11137,2931,11138,2932,11139,11140,2933,11141,2934,11142,2935,11143,2936,11144,2937,11145,2938,11146,2939,11147,2940,11148,2941,11149,11150,2942,11151,2943,11152,2944,11153,2945,11154,2946,11155,2947,11156,2948,11157,2949,11158,2950,11159,2951,11160,11161,2952,11162,2953,11163,2954,11164,2955,11165,2956,11166,2957,11167,2958,11168,2959,11169,2960,11170,11171,2961,11172,2962,11173,2963,11174,2964,11175,2965,11176,2966,11177,2967,11178,2968,11179,2969,11180,2970,11181,11182,2971,11183,2972,11184,2973,11185,2974,11186,2975,11187,2976,11188,2977,11189,2978,11190,2979,11191,11192,2980,11193,2981,11194,2982,11195,2983,11196,2984,11197,2985,11198,2986,11199,2987,11200,2988,11201,2989,11202,11203,2990,11204,2991,11205,2992,11206,2993,11207,2994,11208,2995,11209,2996,11210,2997,11211,2998,11212,11213,2999,11214,3000,11215,3001,11216,3002,11217,3003,11218,3004,11219,3005,11220,3006,11221,3007,11222,3008,11223,11224,3009,11225,3010,11226,3011,11227,3012,11228,3013,11229,3014,11230,3015,11231,3016,11232,3017,11233,11234,3018,11235,3019,11236,3020,11237,3021,11238,3022,11239,3023,11240,3024,11241,3025,11242,3026,11243,3027,11244,11245,3028,11246,3029,11247,3030,11248,3031,11249]

bots =[ 11621,3294,11622,2785,2791,10913,2792,10914,2793,2811,10947,2812,10948,2813,10949,2814,10950,2815,2833,10983,2834,10984,2835,2853,11017,2854,11018,2855,11019,2856,11020,2857,2875,11053,2876,11054,2877,2895,11090,2898,11089,2897,11088,2896,11087,2899,2917,11123]

tops=[11494,3178,11493,3177,3159,11459,3158,11460,3157,3139,11423,3136,11424,3137,11425,3138,11426,3135,3117,11389,3116,11390,3115,3097,11353,3094,11354,3095,11355,3096,11356,3093,3075,11319,3074,11320,3073,3055,11283,3052,11284,3053,11285,3054,11286,3051,3033,11250]



# mdb.models['Model-1'].rootAssembly.SetFromNodeLabels(name='backs427', 
#     nodeLabels=(('Part-1-1', [427]), ))
    
create_pbc_constraints(fronts=fronts, backs=backs, bots=bots, tops=tops)
