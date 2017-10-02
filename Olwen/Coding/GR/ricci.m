(* :Title: Ricci *)

(* :Author: Juan M. Aguirregabiria *)

(* :Summary:   Basic definitions for the calculation, in a 

coordinate frame, of the   contravariant metric tensor, 

Christoffel symbols, Riemann, Ricci and Einstein   tensors 

and the scalar curvature, for a given metric in arbitrary 

dimension. *)

(* :Context: Ricci` *)    (* :Package Version: 1.2 *)

(* :Copyright: Copyright 1989 Juan M. Aguirregabiria *)

(* :History:   Version 1.2, June     1990. Derivative name 

changed!   Version 1.1, April    1990.   Version 1.0, 

December 1989. *)

(* :Keywords:   differential geometry, riemannian geometry, 

general relativity,   Riemann tensor, Ricci tensor, Einstein 

equations, coordinate frame,   affine connection, 

Christoffel symbols *)

(* :Source:   C.W. Misner, K.S. Thorne and J.A. Wheeler, 

"Gravitation", Freeman,   San Francisco (1973). *)

(* :Warning:   According to the standard mathematical 

notation for the Riemann   tensor, the contravariant index 

will be always the first one,   instead of being the last 

one as usual in Mathematica. *)

(* :Mathematica Version: 1.1 and 1.2 *)

(* :Discussion:

    Usage:     1. Needs["Ricci`"]
	2. Introduce the appropriate auxiliary definitions,  
functions... 

	3. Set FirstIndex, LastIndex, and RicciSimplify,if their  
default 

      		values are not appropriate.
	4. Introduce the name of each Coordinate.
	5. Introduce the essential non-null components of the  
MetricTensor.
	6. Define the appropriate transformation rules, ...
	
     	You then dispose of InverseMetric, CovariantChristoffel,  
Christoffel,      

	CovariantRiemann, Riemann, Ricci, ScalarCurvature and  
Einstein.
	But if you prefer to compute systematically all these  
quantities: 

	
	7. Use ComputeRicciPackage[] or, in turn,  
ComputeInverseMetric[],       

		ComputeCovariantChristoffel[], ComputeChristoffel[],      

		ComputeRiemann[], ComputeRicci[],      

		ComputeScalarCurvature[] and ComputeEinstein[].
	8. Use SaveRicci["file"] to save the results for later use,  
if  

		necessary.        

	9. Use ClearRicciPackage[] to reset the package before a new  
problem is
      		analyzed. 


See the example in RicciX.m, which can also be used as a template  
file for
other problems.            


This package and the definitions and conventions used are 

described in the   paper entitled "Computing the Ricci and 

Einstein tensors", by the same   author. *) 


    

BeginPackage["Ricci`"]

FirstIndex::usage = "   FirstIndex is the label of the last 

coordinate.   Usually 0 (the default value) or 1."

LastIndex::usage = "   LastIndex is the label of the last 

coordinate.   LastIndex = FirstIndex+Dimension-1. By default 

3."

Coordinate::usage = "   Coordinate[i] is the name for the 

i-th coordinate."

MetricTensor::usage = "   MetricTensor[i,j] are the 

components of the covariant metric."

InverseMetric::usage = "   InverseMetric[i,j] are the 

components of the contravariant metric."

CovariantChristoffel::usage = "   

CovariantChristoffel[i,j,k] are the connection symbols   

with all their indices lowered."    


Christoffel::usage = "   Christoffel[i,j,k] are the 

connection symbols.   The first index is the contravariant 

one."    


CovariantRiemann::usage = "   CovariantRiemann[i,j,k,l] are 

the   covariant components of the Riemann tensor."

Riemann::usage = "   Riemann[i,j,k,l] are the components of 

the Riemann tensor.   The first index is the contravariant 

one."    


Ricci::usage = "   Ricci[i,j] are the components of the 

Ricci tensor."

ScalarCurvature::usage = "   ScalarCurvature is the 

contraction of the Ricci tensor with the metric."

Einstein::usage = "   Einstein[i,j] are the components of 

the Einstein tensor."

RicciSimplify::usage = "   RicciSimplify is the 

simplification function   to be applied at each step in the 

Ricci package."  


ComputeInverseMetric::usage = "   

ComputeInverseMetric[] generates the contravariant metric 

tensor."

ComputeCovariantChristoffel::usage = "   

ComputeCovariantChristoffel[] generates the   covariant 

connection symbols."

ComputeChristoffel::usage = "   ComputeChristoffel[] 

generates the connection symbols."

ComputeRiemann::usage = "   ComputeRiemann[] generates the 

(covariant) Riemann tensor."

ComputeRicci::usage = "   ComputeRicci[] generates the Ricci 

tensor."

ComputeScalarCurvature::usage = "   ComputeScalarCurvature[] 

generates the scalar curvature."

ComputeEinstein::usage = "   ComputeEinstein[] generates the 

Einstein tensor."

ComputeRicciPackage::usage = "   ComputeRicciPackage[] 

generates all the quantities in the Ricci package."

SaveRicci::usage = "   SaveRicci[file] saves in file   all 

the quantities in the Ricci package."

ClearRicciPackage::usage = "   ClearRicciPackage[] resets 

the Ricci package   before a new metric is analyzed."


Begin["`Private`"]

ClearRicciPackage[] := (

FirstIndex = 0;

LastIndex = 3;

RicciSimplify = Together;

Clear[Coordinate];

Clear[MetricTensor];

Block[   {i,j},
   Do [MetricTensor[i,j] = 0,{i,FirstIndex,LastIndex},       

       {j,i,LastIndex}];
   ];

SetAttributes[MetricTensor,Orderless];

Clear[InverseMetric];

SetAttributes[InverseMetric,Orderless];

(* :Note:   The InverseMetric is computed only once. *)

InverseMetric[k_,l_] := Block[   {i,j,InverseMatrix},   

InverseMatrix =     Inverse[Table[MetricTensor[i,j],  
{i,FirstIndex,LastIndex},                                     

	{j,FirstIndex,LastIndex}]];   

	  

Do [
	InverseMetric[i,j] =  
InverseMatrix[[i-FirstIndex+1,j-FirstIndex+1]] //         

          RicciSimplify,{i,FirstIndex,LastIndex},{j,i,LastIndex}];          

          InverseMetric[k,l]
	];

ComputeInverseMetric[] := (InverseMetric[FirstIndex,FirstIndex];);  



Clear[CovariantChristoffel]; Clear[Christoffel];

CovariantChristoffel[i_,j_,k_] :=CovariantChristoffel[i,k,j]   /; j >  
k;
 	 

Christoffel[i_,j_,k_] := Christoffel[i,k,j] /;j > k;           

 	

(* :Note:   Several quantities are computed only once *)

CovariantChristoffel[p_,q_,r_] := 

Block[   {i,j,k,l,der},   

	Do [
		der[i,j,k] = der[j,i,k] =  
D[MetricTensor[i,j],Coordinate[k]] //       

  		 
RicciSimplify,{i,FirstIndex,LastIndex},{j,i,LastIndex},                     

			{k,FirstIndex,LastIndex}];

		Do [
		 
CovariantChristoffel[i,j,k]=(der[i,j,k]+der[i,k,j]-der[j,k,i])/2 //                    

			RicciSimplify,
			{i,FirstIndex,LastIndex},       

			{j,FirstIndex,LastIndex},
			{k,j         ,LastIndex}
		];
			    

		CovariantChristoffel[p,q,r]
	];

ComputeCovariantChristoffel[] :=   

(CovariantChristoffel[FirstIndex,FirstIndex,FirstIndex];);

Christoffel[p_,q_,r_] := 

Block[   {i,j,k,l},   

	Do [
		 
Christoffel[i,j,k]=Sum[InverseMetric[i,l]CovariantChristoffel[l,j,k],             

			{l,FirstIndex,LastIndex}] // 

			RicciSimplify,       

			{i,FirstIndex,LastIndex},
			{j,FirstIndex,LastIndex},       

			{k,j,LastIndex}
		];   

		
		Christoffel[p,q,r]
	];

ComputeChristoffel[] :=  
(Christoffel[FirstIndex,FirstIndex,FirstIndex];);  



Clear[CovariantRiemann];

CovariantRiemann[i_,i_,k_,l_] :=  0;        

CovariantRiemann[i_,j_,k_,k_] :=  0;        

CovariantRiemann[i_,j_,k_,l_] := -CovariantRiemann[j,i,k,l] /; i > j;     

CovariantRiemann[i_,j_,k_,l_] := -CovariantRiemann[i,j,l,k] /; k > l;
 

CovariantRiemann[i_,j_,k_,l_] :=  CovariantRiemann[k,l,i,j] /;    

	i < j && k < l && (i > k || (i == k && j > l));
	
CovariantRiemann[i_,j_,k_,l_] :=
	CovariantRiemann[i,l,k,j]-CovariantRiemann[i,k,l,j] /; (i < k  
< l < j);                                                         



CovariantRiemann[i_,j_,k_,l_] := CovariantRiemann[i,j,k,l] = 

Block[   {m},

	D[CovariantChristoffel[i,j,l],Coordinate[k]] -
	D[CovariantChristoffel[i,j,k],Coordinate[l]] +   

	Sum[Christoffel[m,i,l] CovariantChristoffel[m,j,k] -       

		Christoffel[m,i,k] CovariantChristoffel[m,j,l] ,       

		{m,FirstIndex,LastIndex}] 

	// RicciSimplify];
	

ComputeRiemann[] := 

Block[   {i,j,k,l},
	Do [
		If [j <= l,
			CovariantRiemann[i,j,k,l]
		],
		
		 
{i,FirstIndex,LastIndex-1},{j,i+1,LastIndex},{k,i,LastIndex-1}, 

          {l,k+1,LastIndex  }];
		
];

Riemann[i_,j_,k_,l_] := 

	Block[   {m},
   

	Sum[InverseMetric[i,m] CovariantRiemann[m,j,k,l],       

		{m,FirstIndex,LastIndex}] // RicciSimplify
	];
	

Clear[Ricci];

SetAttributes[Ricci,Orderless];

Ricci[i_,j_] := Ricci[i,j] = 

	Block[ {k},	   

		Sum[Riemann[k,i,k,j],{k,FirstIndex,LastIndex}] //  
RicciSimplify		
	];


ComputeRicci[] := 

	Block[ {i,j},
		Do [
			Ricci[i,j],       

			{i,FirstIndex,LastIndex},{j,i,LastIndex}
		];
	];

Clear[ScalarCurvature];

ScalarCurvature := ScalarCurvature = 

	Block[ {i,j},
	   

		Sum[InverseMetric[i,j] Ricci[i,j],{i,FirstIndex,LastIndex}, {j,FirstIndex,LastIndex}] // RicciSimplify
	];

ComputeScalarCurvature[] := (ScalarCurvature;);

Clear[Einstein];

SetAttributes[Einstein,Orderless];

Einstein[i_,j_] := Einstein[i,j] =   

	Ricci[i,j]- ScalarCurvature/2 MetricTensor[i,j] //  
RicciSimplify;

ComputeEinstein[] := 

	Block[{i,j},
		Do [
			Einstein[i,j],       

				 
{i,FirstIndex,LastIndex},{j,i,LastIndex}
		];
	];


ComputeRicciPackage[] := (   

	Print["Computing the inverse metric"];
   	ComputeInverseMetric[];
	Print["Computing the connection"];
	ComputeCovariantChristoffel[];   

	ComputeChristoffel[];
	Print["Computing the Riemann tensor"];
	ComputeRiemann[];
	Print["Computing the Ricci tensor"];
	ComputeRicci[];
	Print["Computing the scalar curvature"];
	ComputeScalarCurvature[];
	Print["Computing the Einstein tensor"];
	ComputeEinstein[];
	);

SaveRicci[file_] :=   

	Save[file,
     	FirstIndex,        

		LastIndex,
		Coordinate,
		MetricTensor,        

		InverseMetric,
		CovariantChristoffel,        

		Christoffel,
		CovariantRiemann,
		Riemann,        

		Ricci,
		ScalarCurvature,
		Einstein];

);                      


(* :Note:   End of ClearRicciPackage and do it! *)

ClearRicciPackage[];

End[]

EndPackage[]

