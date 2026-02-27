from unimod_lookup import UniMod
import PARAMETERS as CON
from pyteomics import mass
import re

class ModifiedMassComputer:
    """
    parses peptide string with (UniMod:tag) kind codes and computes their 
    average mass taking into account the modification
    """
    
    unimod = UniMod.default()
    mod_matcher = re.compile(r"\(UniMod:(\d+)\)")
    
    def __init__(self, umod=None):
        if umod is not None:
            self.uni_db = umod
        else:
            self.uni_db = self.unimod
    
    def parse_monoisotopic(self, peptide :str):
        """
        parse each peptide, whether modified or not
        into a generator sequence of corresponding mono-isotopic mass values
        based on pyteomics mass.fast_mass and the UniMod database we carry locally
        """
        curr_idx = 0
        while curr_idx < len(peptide):
            sym_here = peptide[curr_idx]
            if sym_here in CON.PEPTIDE_MASS_DICTIONARY:
                #yield CON.PEPTIDE_MASS_DICTIONARY[sym_here]
                yield mass.fast_mass(sym_here)
                curr_idx += 1
            elif sym_here == '(':
                # get the mass change from the modification
                end_modtag = peptide.find(')',curr_idx)
                modtag = peptide[curr_idx:end_modtag+1]
                mod_match = self.mod_matcher.match(modtag)
                mod_id = mod_match.groups()[0]
                modification = self.uni_db[mod_id]
                mod_mono_iso_mass = float(modification['mono_mass'])
                #mod_avg_mass = float(modification["avge_mass"])
                # get the peptide being modified and its mass
                curr_idx = end_modtag+1
                # account for terminal modifications which may be present
                # after the last peptide
                if curr_idx < len(peptide):
                    pep_sym = peptide[curr_idx]
                    pep_basemass = mass.fast_mass(pep_sym)
                    #pep_basemass = CON.PEPTIDE_MASS_DICTIONARY[pep_sym]
                    # apply the modification
                    modified_mass = pep_basemass + mod_mono_iso_mass
                    yield modified_mass
                    curr_idx += 1
                else:
                    # no following peptide, but there is a trailing modification which has a mass
                    yield mod_mono_iso_mass
            else:
                raise RuntimeError(
                    "Encountered unexpected symbol {} during peptide parsing, likely issue in parser".format(
                        sym_here
                    )
                )
    
    def compute_mass_monoisotopic(self, peptide :str):
        mass = 0
        for pep_mass in self.parse_monoisotopic(peptide):
            mass += pep_mass
        # monoisotopic mass of water is also average mass of water
        mass += CON.MASS_OF_WATER
        return mass
    
    def parse_avg(self, peptide :str):
        """
        parse each peptide, whether modified or not,
        into a generator sequence of corresponding average mass values
        based on the parameters file and the modification database
        """
        curr_idx = 0
        while curr_idx < len(peptide):
            sym_here = peptide[curr_idx]
            if sym_here in CON.PEPTIDE_MASS_DICTIONARY:
                yield CON.PEPTIDE_MASS_DICTIONARY[sym_here]
                curr_idx += 1
            elif sym_here == '(':
                # get the mass change from the modification
                end_modtag = peptide.find(')',curr_idx)
                modtag = peptide[curr_idx:end_modtag+1]
                mod_match = self.mod_matcher.match(modtag)
                mod_id = mod_match.groups()[0]
                modification = self.uni_db[mod_id]
                mod_avg_mass = float(modification["avge_mass"])
                # get the peptide being modified and its mass
                curr_idx = end_modtag+1
                # account for terminal modifications which may be present
                # after the last peptide
                if curr_idx < len(peptide):
                    pep_sym = peptide[curr_idx]
                    pep_basemass = CON.PEPTIDE_MASS_DICTIONARY[pep_sym]
                    # apply modified mass
                    modified_mass = pep_basemass + mod_avg_mass
                    yield modified_mass
                    curr_idx += 1
                else:
                    # no following peptide, but there is a modification, which has a mass
                    yield mod_avg_mass
            else:
                raise RuntimeError(
                    "Encountered unexpected symbol {} during peptide parsing, likely issue in parser".format(
                        sym_here
                    )
                )
    
    def compute_mass_avg(self, peptide :str) -> float:
        """
        Compute the average mass of a peptide, taking into account 
        modifications of format (UniMod:modID)
        """
        mass = 0
        for pep_mass in self.parse_avg(peptide):
            mass += pep_mass
        mass += CON.MASS_OF_WATER
        return mass
