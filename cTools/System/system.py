import multiprocessing, platform

Class System():
  def __init__(self, run_as_admin:bool=False):
    self.run_as_admin = run_as_admin
    
  class Hardware:
    class CPU:
      def get_cores():
        """
        Returns the amount of CPU Cores
        """
        return multiprocessing.cpu_count()
      
      def get_cpu_info():
        """
        Returns a dictionary with CPU Information
        """
        cpu_info = {}
    
        cpu_info['Processor'] = platform.processor()
        cpu_info['Architecture'] = platform.architecture()[0]
        cpu_info['Cores'] = multiprocessing.cpu_count()
        cpu_info['Machine'] = platform.machine()
        cpu_info['System'] = platform.system()
        cpu_info['Processor Identifier'] = platform.processor()
    
        return cpu_info
      
      def get_cpu_processor():
        return platform.processor()
      
      def get_cpu_architecture():
        return platform.architecture()[0]
    
    class Memory:
      None
    
    class GPU:
      None
      
    class Storage:
      None
    
    class Power:
      None
