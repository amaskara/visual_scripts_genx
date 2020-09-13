# genx_path = "/home/jdj2/GenX_Rescaled_11_30_19/"
genx_path = "/tigress/patankar/GenX/PJM/PJM_Aug_20/"
working_path = pwd()
settings_path = joinpath(pwd(), "GenX_settings.yml")
println(settings_path)
push!(LOAD_PATH, genx_path, working_path)

using GenX
using DataFrames
using YAML
using Dates
using CSV

println(now())

mysetup = YAML.load(open(settings_path))

case_path = pwd()
inpath = joinpath(case_path, "Inputs")
outpath = joinpath(case_path, "Results")

# Copy GenX to case folder to facilitate reproduction of case
#cp(joinpath(genx_path, "GenX.jl"), joinpath(case_path, "GenX_archive.jl"), force=true)

# Running a case

  myinputs=Dict()
  #loading general inputs
  myinputs = load_inputs(mysetup,inpath)
  # creation of optimization instance and solution
  myresults = solve_model(mysetup,myinputs, genx_path)
  # # writing output
  write_outputs(mysetup,outpath,myresults,myinputs)
  myresults["CAP"][:new_ID]="NA"
  myresults["CAP"][:new_ID][1:myinputs["G"]] = myinputs["dfGen"][:region] .* "_" .* myinputs["dfGen"][:Resource] .* "_" .* myinputs["dfGen"][:cluster]

#Modifying inputs for stage 2 - 2040
  inpath2="/tigress/patankar/GenX/PJM/PJM_Aug_20/2040/p2_2040_statedpolicy/Inputs"
  outpath2="/tigress/patankar/GenX/PJM/PJM_Aug_20/2040/p2_2040_statedpolicy/Results"
  myinputs=Dict()
  myinputs = load_inputs(mysetup,inpath2)
  myinputs["dfGen"][:new_ID] = myinputs["dfGen"][:region] .* "_" .* myinputs["dfGen"][:Resource] .* "_" .* myinputs["dfGen"][:cluster]

  for i in myinputs["dfGen"][:new_ID]
    if (i in myresults["CAP"][:new_ID]) .& (i in myinputs["dfGen"][:new_ID][myinputs["dfGen"][:Resource].∉Ref(["DER_Solar","ev_load_shifting","heat_load_shifting"]),:])
      myinputs["dfGen"][(myinputs["dfGen"][!,:new_ID].==i),:Existing_Cap_MWh] = max(floor.(myresults["CAP"][(myresults["CAP"][!,:new_ID].==i),:EndEnergyCap], digits=0),[0])
      myinputs["dfGen"][(myinputs["dfGen"][!,:new_ID].==i),:Existing_Charge_Cap_MW] = max(floor.(myresults["CAP"][(myresults["CAP"][!,:new_ID].==i),:EndChargeCap], digits=0),[0])
      myinputs["dfGen"][(myinputs["dfGen"][!,:new_ID].==i),:Existing_Cap_MW] = max(floor.(myresults["CAP"][(myresults["CAP"][!,:new_ID].==i),:EndCap], digits=0),[0])
    end
  end

  myinputs["pTrans_Max"] = round.(myresults["TRANS_CAP"][!,:New_Trans_Capacity], digits=0) + myinputs["pTrans_Max"]
  pNew_Trans_Capacity_2030 = round.(myresults["TRANS_CAP"][!,:New_Trans_Capacity], digits=0)

# write the new Generators data file for stage 2
  #solve the stage 2 model with new inputs
  myresults = solve_model(mysetup,myinputs)
  # # writing output stage 2
  write_outputs(mysetup,outpath2,myresults,myinputs)
  myresults["CAP"][:new_ID]="NA"
  myresults["CAP"][:new_ID][1:myinputs["G"]] = myinputs["dfGen"][:region] .* "_" .* myinputs["dfGen"][:Resource] .* "_" .* myinputs["dfGen"][:cluster]

 #Modifying inputs for stage 3 - 2050
  inpath3="/tigress/patankar/GenX/PJM/PJM_Aug_20/2050/p2_2050_statedpolicy/Inputs"
  outpath3="/tigress/patankar/GenX/PJM/PJM_Aug_20/2050/p2_2050_statedpolicy/Results"
  myinputs=Dict()
  myinputs = load_inputs(mysetup,inpath3)
  myinputs["dfGen"][:new_ID] = myinputs["dfGen"][:region] .* "_" .* myinputs["dfGen"][:Resource] .* "_" .* myinputs["dfGen"][:cluster]

  for i in myinputs["dfGen"][:new_ID]
    if (i in myresults["CAP"][:new_ID]) .& (i in myinputs["dfGen"][:new_ID][myinputs["dfGen"][:Resource].∉Ref(["DER_Solar","ev_load_shifting","heat_load_shifting"]),:])
      myinputs["dfGen"][(myinputs["dfGen"][!,:new_ID].==i),:Existing_Cap_MWh] = max(floor.(myresults["CAP"][(myresults["CAP"][!,:new_ID].==i),:EndEnergyCap], digits=0),[0])
      myinputs["dfGen"][(myinputs["dfGen"][!,:new_ID].==i),:Existing_Charge_Cap_MW] = max(floor.(myresults["CAP"][(myresults["CAP"][!,:new_ID].==i),:EndChargeCap], digits=0),[0])
      myinputs["dfGen"][(myinputs["dfGen"][!,:new_ID].==i),:Existing_Cap_MW] = max(floor.(myresults["CAP"][(myresults["CAP"][!,:new_ID].==i),:EndCap], digits=0),[0])
    end
  end

  myinputs["pTrans_Max"] = round.(myresults["TRANS_CAP"][!,:New_Trans_Capacity], digits=0) + myinputs["pTrans_Max"] + pNew_Trans_Capacity_2030

  #solve the stage 3 model with new inputs
  myresults = solve_model(mysetup,myinputs)
  # # writing output stage 3
  write_outputs(mysetup,outpath3,myresults,myinputs)
