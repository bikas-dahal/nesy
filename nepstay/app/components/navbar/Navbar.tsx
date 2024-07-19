import Image from 'next/image';
import Link from 'next/link';

// import SearchFilters from './SearchFilters';
// import UserNav from './UserNav';
// // import { getUserId } from '@/app/lib/actions';
// import AddPropertyButton from './AddPropertyButton';

const Navbar = async () => {

    return (
        <nav className="w-full fixed top-0 left-0 py-6 border-b bg-white z-10">
            <div className="text-nepal max-w-[1500px] mx-auto px-6">
                <div className="flex justify-between items-center">
                    <Link href="/">
                        <Image
                            src="/logo.png"
                            alt="NepStay logo"
                            width={80}
                            height={38}
                        />
                    </Link>

                </div>
            </div> 
        </nav>   
    )
}

export default Navbar;