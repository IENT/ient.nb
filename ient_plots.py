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
import matplotlib.colors as mcolors

import numpy as np

#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')

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
        shadow_transform = l.get_transform() + offset
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
    ax.xaxis.label.set_verticalalignment('bottom')
    ax.xaxis.label.set_horizontalalignment('right')
    
    ax.yaxis.label.set_rotation(0)
    on_ylims_change()
    ax.yaxis.label.set_verticalalignment('top')
    ax.yaxis.label.set_horizontalalignment('left')
    
    ax.xaxis.label.set_fontsize(12)
    ax.yaxis.label.set_fontsize(12)


# annotate certain xtick
def ient_annotate_xtick(ax,txt, x,y,col,fs=12):
    txt_ret = ax.text(x,y,txt, color=col, fontsize=fs, verticalalignment='top', horizontalalignment='center',
                     bbox=dict(facecolor='white', edgecolor='none', alpha=0.75));
    line_ret, = ax.plot([x,x],[0,y],'--', color=col, lw=0.5)

# grid
def ient_grid(ax):
    ax.grid(); ax.set_axisbelow(True);

def ient_update_xlim(ax,x,dx,xmax=5):
    ax.set_xlim([np.max([np.min(x),-xmax])-dx, np.min([np.max(x),xmax])+dx])
        
def ient_update_ylim(ax,y,dy,ymax=5):
    ax.set_ylim([np.max([np.min(y),-ymax])-dy, np.min([np.max(y),ymax])+dy])
        
# RWTH Colors
rwth_colors = {
    'rwth'    : '#00549F',
    'rwth-75' : '#407FB7',
    'rwth-50' : '#8EBAE5',
    'rwth-25' : '#C7DDF2',
    'rwth-10' : '#E8F1FA', 
    'black'    : '#000000',
    'black-75' : '#646567',
    'black-50' : '#9C9E9F',
    'black-25' : '#CFD1D2',
    'black-10' : '#ECEDED',
    'magenta'    : '#E30066',
    'magenta-75' : '#E96088',
    'magenta-50' : '#F19EB1',
    'magenta-25' : '#F9D2DA',
    'magenta-10' : '#FDEEF0',
    'yellow'    : '#FFED00',
    'yellow-75' : '#FFF055',
    'yellow-50' : '#FFF59B',
    'yellow-25' : '#FFFAD1',
    'yellow-10' : '#FFFDEE',
    'petrol'    : '#006165',
    'petrol-75' : '#2D7F83',
    'petrol-50' : '#7DA4A7',
    'petrol-25' : '#BFD0D1',
    'petrol-10' : '#E6ECEC',
    'turkis'    : '#0098A1',
    'turkis-75' : '#00B1B7',
    'turkis-50' : '#89CCCF',
    'turkis-25' : '#CAE7E7',
    'turkis-10' : '#EBF6F6',
    'grun'    : '#57AB27',
    'grun-75' : '#8DC060',
    'grun-50' : '#B8D698',
    'grun-25' : '#DDEBCE',
    'grun-10' : '#F2F7EC',
    'maigrun'    : '#BDCD00',
    'maigrun-75' : '#D0D95C',
    'maigrun-50' : '#E0E69A',
    'maigrun-25' : '#F0F3D0',
    'maigrun-10' : '#F9FAED',
    'orange'    : '#F6A800',
    'orange-75' : '#FABE50',
    'orange-50' : '#FDD48F',
    'orange-25' : '#FEEAC9',
    'orange-10' : '#FFF7EA',
    'rot'    : '#CC071E',
    'rot-75' : '#D85C41',
    'rot-50' : '#E69679',
    'rot-25' : '#F3CDBB',
    'rot-10' : '#FAEBE3',
    'bordeaux'    : '#A11035',
    'bordeaux-75' : '#B65256',
    'bordeaux-50' : '#CD8B87',
    'bordeaux-25' : '#E5C5C0',
    'bordeaux-10' : '#F5E8E5',
    'violett'    : '#612158',
    'violett-75' : '#834E75',
    'violett-50' : '#A8859E',
    'violett-25' : '#D2C0CD',
    'violett-10' : '#EDE5EA',
    'lila'    : '#7A6FAC',
    'lila-75' : '#9B91C1',
    'lila-50' : '#BCB5D7',
    'lila-25' : '#DEDAEB',
    'lila-10' : '#F2F0F7',
}

#rwth_colors = {'rwth:' + name: value for name, value in RWTH_COLORS.items()}

# Propagate rwth_colors to default matplotlib colors
mcolors.get_named_colors_mapping().update(rwth_colors)

# Widget label style (full width)
ient_wdgtl_style = {'description_width': 'initial'}

# Axis white background
ient_wbbox = {"facecolor": "white", "edgecolor": "None", "pad": 0}