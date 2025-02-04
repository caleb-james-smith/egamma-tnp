# make_plots.py

import pickle
import matplotlib.pyplot as plt
import tools

def main():
    input_file = "egamma_test_2025_02_03_run_2/EGamma0_Run2023C-22Sep2023_v1-v1_NANOAOD/get_1d_pt_eta_phi_tnp_histograms_1/HLT_Ele30_WPTight_Gsf_histos.pkl"
    output_file = "mll_vs_pt_barrel_passing"
    plot_dir = "plots"
    
    tools.makeDir(plot_dir)

    with open(input_file, "rb") as f:
        histCollection = pickle.load(f)
    
    #print("histCollection:")
    #print(histCollection)

    printKeys(histCollection)

    hist = histCollection['pt']['barrel']['passing']

    plotHist(hist, plot_dir, output_file)

def printKeys(histCollection):
    print("Keys:")
    for key_1 in histCollection:
        print(" - {0}".format(key_1))
        for key_2 in histCollection[key_1]:
            print("  - {0}".format(key_2))
            for key_3 in histCollection[key_1][key_2]:
                print("   - {0}".format(key_3))

def plotHist(hist, plot_dir, output_file):
    # Create a figure and an axes object
    fig, ax = plt.subplots()
    hist.plot()
    
    output_png = "{0}/{1}.png".format(plot_dir, output_file)
    output_pdf = "{0}/{1}.pdf".format(plot_dir, output_file)

    plt.savefig(output_png, bbox_inches='tight')
    plt.savefig(output_pdf, bbox_inches='tight')

    # close to avoid memory warning 
    plt.close('all')

if __name__ == "__main__":
    main()

