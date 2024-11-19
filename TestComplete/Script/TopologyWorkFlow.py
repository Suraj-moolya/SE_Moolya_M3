"""TopologyWorkFlow"""  

from Topology import Topology
import Applicationutility
import Topologyexplorerutility
class TopologyWorkFlow:
    """TopologyWorkFlow"""
    topology_obj = Topology()

        
    def textboxnewpasswordboxentercontrollerpasswordte(self,param):
        """textboxnewpasswordboxentercontrollerpasswordte"""
        try:
            Topologyexplorerutility.Enter_Controller_Password_TE(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxnewpasswordboxverifyenteredcontrollerpasswordvalidinvalidte(self,param):
        """textboxnewpasswordboxverifyenteredcontrollerpasswordvalidinvalidte"""
        try:
            Topologyexplorerutility.Verify_entered_Controller_Password_valid_invalid_TE(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
