from matplotlib import rcParams
rcParams["axes.axisbelow"] = False

#rcParams['font.family'] = 'sans-serif'
#rcParams['font.sans-serif'] = ['Arial']
#rcParams['font.size'] = 14
#rcParams['text.usetex'] = True
#rcParams['text.latex.unicode'] = True

from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.gridspec as gridspec
import matplotlib.transforms as trans

import numpy as np

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Style axis
def ient_axis(ax):
    
    #func = lambda x, pos: "" if np.isclose(x,0) else x
    #ax.xaxis.set_major_formatter(ticker.FuncFormatter(func))
    #ax.yaxis.set_major_formatter(ticker.FuncFormatter(func))
    
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    def on_xlims_change(axes=[]):
        ax.xaxis.set_label_coords(ax.get_xlim()[1],0, transform=ax.transData);
        
        dd = 2/72.
        fig = ax.get_figure()
        l = ax.xaxis.label
        xpos, ypos = l.get_position()    
        offset = trans.ScaledTranslation(0, dd, fig.dpi_scale_trans)
        shadow_transform = l.get_transform() - offset
        ax.xaxis.set_label_coords(xpos,ypos, transform=shadow_transform)
        
    def on_ylims_change(axes=[]):
        ax.yaxis.set_label_coords(0,ax.get_ylim()[1], transform=ax.transData);
        
        dd = 2/72.
        fig = ax.get_figure()
        l = ax.yaxis.label
        xpos, ypos = l.get_position()    
        offset = trans.ScaledTranslation(dd, 0, fig.dpi_scale_trans)
        shadow_transform = l.get_transform() + offset
        ax.yaxis.set_label_coords(xpos,ypos, transform=shadow_transform)
    

    ax.callbacks.connect('xlim_changed', on_xlims_change)
    ax.callbacks.connect('ylim_changed', on_ylims_change)
    
    on_xlims_change()
    ax.xaxis.label.set_verticalalignment('top')
    ax.xaxis.label.set_horizontalalignment('right')
    
    ax.yaxis.label.set_rotation(0)
    on_ylims_change()
    ax.yaxis.label.set_verticalalignment('top')
    ax.yaxis.label.set_horizontalalignment('left')
    
    ax.xaxis.label.set_fontsize(12)
    ax.yaxis.label.set_fontsize(12)
   